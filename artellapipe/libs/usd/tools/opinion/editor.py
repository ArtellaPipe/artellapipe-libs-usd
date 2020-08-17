#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Opinion Editor widget implementations
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from Qt.QtCore import *
from Qt.QtWidgets import *

from pxr import Usd
from pxr.UsdQt._bindings import _DisplayGroupProxy, _PrimProxy, _AttributeProxy, _MetadataProxy
from pxr.UsdQt.opinionStackModel import _AttributeHandler, _PrimMetadataHandler
from pxr.UsdQt import valueDelegate, opinionStackModel

from artellapipe.libs.usd.core import usdqtutils


class OpinionEditor(QWidget, object):
    def __init__(self, deleagate=None, parent=None):
        super(OpinionEditor, self).__init__(parent=parent)

        self._menu_bar = QMenuBar()
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self._filter_line_edit = QLineEdit()

        self._view = usdqtutils.SelectionEditTreeView()
        item_delegate = deleagate if deleagate else valueDelegate.ValueDelegate()
        self._view.setItemDelegate(item_delegate)
        self._view.setEditTriggers(
            QAbstractItemView.CurrentChanged | QAbstractItemView.SelectedClicked | QAbstractItemView.EditKeyPressed)
        self._view.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self._splitter = QSplitter(Qt.Vertical, self)
        self._layout.addWidget(self._menu_bar)
        self._layout.addWidget(self._filter_line_edit)
        self._layout.addWidget(self._splitter)
        self._splitter.addWidget(self._view)

        self._setup_actions()
        self._setup_options_menu()
        self._setup_edit_menu()
        self._setup_option_view_widget()

    @property
    def view(self):
        return self._view

    def launch_opinions_viewer(self, prim, handler):
        self._opinion_viewer.launch(opinionStackModel.OpinionStackModel(prim, handler))

    def set_source_model(self, model):
        self._view.setModel(model)
        self.reset_column_spanned()

    def reset_column_spanned(self):
        for index in self._traverse_all_descendents(QModelIndex()):
            if type(index.internalPointer()) in (_DisplayGroupProxy, _PrimProxy):
                self._view.setFirstColumnSpanned(index.row(), index.parent(), True)

    def _traverse_all_descendents(self, index):
        for i in range(self._view.model().rowCount(index)):
            child_index = self._view.model().index(i, 0, index)
            yield child_index
            for descendent in self._traverse_all_descendents(child_index):
                yield descendent

    def _setup_actions(self):
        pass

    def _setup_options_menu(self):
        self._options_menu = QMenu('Options')
        self._menu_bar.addMenu(self._options_menu)

    def _setup_edit_menu(self):
        self._edit_menu = QMenu('Edit')
        self._menu_bar.addMenu(self._edit_menu)

    def _setup_option_view_widget(self):
        self._opinion_viewer = OpinionStackWidget()
        self._options_menu.hide()
        self._splitter.addWidget(self._opinion_viewer)


class OpinionStackWidget(QWidget, object):
    def __init__(self, parent=None):
        super(OpinionStackWidget, self).__init__(parent=parent)

        self._toolbar = QToolBar()
        self._toolbar.addWidget(QLabel('Opinion Stack'))
        self._toolbar.addSeparator()
        self._show_all_action = self._toolbar.addAction('Show All')
        self._show_all_action.setCheckable(True)
        self._close_action = self._toolbar.addAction('Close')
        self._show_all_action.toggled.connect(self._on_show_all_toggled)
        self._close_action.triggered.connect(self._on_close)

        self._opinion_filter = opinionStackModel.OpinionStackFilter()
        self._view = QTreeView()
        self._view.setModel(self._opinion_filter)

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)
        self._layout.addWidget(self._toolbar)
        self._layout.addWidget(self._view)

        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

    def launch(self, model):
        self._opinion_filter.setSourceModel(model)
        self.show()

    def close_(self):
        self.hide()
        self._opinion_filter.setSourceModel(None)

    def _on_show_all_toggled(self, checked):
        self._opinion_filter.SetShowFullStack(checked)

    def _on_close(self):
        self.close_()


class OpinionController(QObject, object):
    def __init__(self, model, editor, parent=None):
        super(OpinionController, self).__init__(parent)

        self._model = model
        self._editor = editor
        self._editor.view.doubleClicked.connect(self._on_double_clicked)

    def reset_prims(self, prims):
        self._model.ResetPrims(prims)
        self._editor.reset_columns_spanned()

    def _on_double_clicked(self, index):
        proxy = self._model.GetProxyForIndex(index)
        if type(proxy) == _AttributeProxy:
            if proxy.GetSize() == 1:
                attributes = proxy.GetAttributes()
                attribute = attributes[0]
                self._editor.launch_opinions_viewer(
                    attribute.GetPrim(), _AttributeHandler(attribute.GetName(), Usd.TimeCode.Default()))
        elif type(proxy) == _MetadataProxy:
            if proxy.GetSize() == 1:
                objects = proxy.GetObjects()
                obj = objects[0]
                if type(obj) == Usd.Prim:
                    self._editor.launch_opinions_viewer(obj, _PrimMetadataHandler(proxy.GetName()))
