#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains Qt related utilities functions related with USD
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import inspect
import logging
import traceback
from functools import partial

from Qt.QtCore import *
from Qt.QtWidgets import *

from pxr import Sdf

LOGGER = logging.getLogger('artellapipe-libs-usd')


class MenuSeparator(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __call__(self, *args, **kwargs):
        return self

    def add_to_menu(self, menu, context, context_callback=None):
        menu.addSeparator()


class MenuAction(object):

    DEFAULT_TEXT = ''

    def __init__(self):
        super(MenuAction, self).__init__()

        self._context_callback = None

    def set_context_callback(self, context_callback):
        self._context_callback = context_callback

    def get_current_context(self):
        if self._context_callback:
            return self._context_callback()

        return None

    def build(self, context):
        text = self.DEFAULT_TEXT or self.__class__.__name__
        action = QAction(text, None)
        self.update(action, context)
        action.triggered.connect(self.do)

        return action

    def update(self, action, context):
        pass

    def add_to_menu(self, menu, context, context_callback=None):
        self.set_context_callback(context_callback)

        action = self.build(context)
        if action is None:
            return

        action.setData(self)
        menu.addAction(action)
        action.setParent(menu)

    def do(self):
        raise NotImplementedError


class MenuBuilder(object):
    def __init__(self, name, actions):
        name = name.strip()
        self._name = name
        action_instances = list()

        for action in actions:
            if isinstance(action, (MenuAction, MenuSeparator)):
                action_instances.append(action)
            elif inspect.isclass(action) and (action is MenuSeparator or issubclass(action, MenuAction)):
                action_instances.append(action())
            else:
                raise TypeError(
                    'Invalid action {0!r}: an instance or subclass of MenuAction is required'.format(action))

        self._actions = action_instances

    @property
    def name(self):
        return self._name

    @property
    def actions(self):
        return self._actions

    def build(self, context, context_callback=None, parent=None):
        menu = QMenu(self._name, parent)
        for action in self._actions:
            action.add_to_menu(menu, context, context_callback=context_callback)
        if not menu.isEmpty():
            return menu

        return None


class ContextMenuMixin(object):
    def __init__(self, context_menu_actions, context_provider=None, parent=None):
        super(ContextMenuMixin, self).__init__(parent=parent)

        assert isinstance(self, QWidget)

        self._context_provider = context_provider
        self._context_menu_builder = MenuBuilder('_context_', context_menu_actions)

    def contextMenuEvent(self, event):
        context = self.get_menu_context()
        menu = self._context_menu_builder.build(context, context_callback=self.get_menu_context, parent=self)
        if menu:
            menu.exec_(event.globalPos())
            event.accept()

    def get_menu_context(self):
        if self._context_provider:
            return self._context_provider.get_menu_context()

        raise NotImplementedError('No context provider set and get_menu_context not reimplemented')


class MenuBarBuilder(object):
    def __init__(self, context_provider, menu_builders=None, parent=None):
        super(MenuBarBuilder, self).__init__()

        self._context_provider = context_provider
        self._menus = dict()
        self._menu_builders = dict()

        if hasattr(parent, 'menuBar'):
            self._menu_bar = parent.menuBar()
        else:
            self._menu_bar = QMenuBar(parent=parent)
        if menu_builders:
            context = self._context_provider.get_menu_context()
            for builder in menu_builders:
                self.add_menu(builder, context)

    @property
    def menu_bar(self):
        return self._menu_bar

    def add_menu(self, menu_builder, context):
        name = menu_builder.name
        if name in self._menus:
            raise ValueError('A menu named {} already exists!'.format(name))
        menu = menu_builder.build(
            context, context_callback=self._context_provider.get_menu_context, parent=self._menu_bar)
        if menu:
            self._menu_bar.addMenu(menu)
            menu.aboutToShow.connect(partial(self._on_menu_about_to_show, name))
            self._menus[name] = menu
            self._menu_builders[name] = menu_builder
            return True

        return False

    def get_menu(self, name):
        return self._menus.get(name, None)

    def get_menu_builder(self, name):
        return self._menu_builders.get(name, None)

    def _on_menu_about_to_show(self, name):
        menu = self.get_menu(name)
        if not menu:
            return

        context = self._context_provider.get_menu_context()
        for action in menu.actions():
            if action.isSeparator():
                continue
            action_data = action.data()
            if action_data and isinstance(action_data, MenuAction):
                action_data.update(action, context)


class SelectionEditTreeView(QTreeView, object):
    """
    Custom QTreeView implementation to add selection edit based functionality.
    Selection edits allow editing of all selected attributes simultaneously.
    """

    SelectedEditOff = 0
    SelectedEditColumnsOnly = 1

    def __init__(self, parent=None):
        super(SelectionEditTreeView, self).__init__(parent=parent)

        self._selection_edit_mode = SelectionEditTreeView.SelectedEditColumnsOnly

    def commitData(self, editor):
        # TODO: Add an UndoBlock

        editor_index = None
        if self.indexWidget(self.currentIndex()) == editor:
            editor_index = self.currentIndex()

        if not editor_index:
            super(SelectionEditTreeView, self).commitData(editor)
            return

        selection = None
        if self._selection_edit_mode == SelectionEditTreeView.SelectedEditColumnsOnly:
            selection = [i for i in self.selectionModel().selectedIndexes()
                         if i.column() == editor_index.column() and i != editor_index]

        # It's important to put all edits inside of an Sdf Change Block so they happen in a single pass and
        # no signals are emitted that may change state
        with Sdf.ChangeBlock():
            super(SelectionEditTreeView, self).commitData(editor)
            if selection:
                value = editor.value
                for index in selection:
                    # This try / except is covering for a very ugly and hard to isolate bug.  It appears that when
                    # commitData raises an exception, Qt holds onto some indices that should safely expire, triggering
                    # a deferred but hard crash.  I haven't found a reliable repro case, but this seems to make it
                    # go away.  A better solution likely involves better detection on the model side.
                    try:
                        self.model().setData(index, value, Qt.EditRole)
                    except Exception:
                        LOGGER.exception('Exception during multi-edit: {}'.format(traceback.format_exc()))

    def set_selected_edit_mode(self, mode):
        self._selection_edit_mode = mode
