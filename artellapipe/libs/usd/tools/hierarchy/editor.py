#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Hierarchy Editor widget implementations
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from collections import OrderedDict

from Qt.QtCore import *
from Qt.QtWidgets import *

from pxr.UsdQt import hierarchyModel, roles

from artellapipe.libs.usd.tools.hierarchy import actions


class HierarchyEditor(QWidget, object):

    SHOW_INACTIVE = 'Show Inactive'
    SHOW_UNDEFINED = 'Show Undefined (Overs)'
    SHOW_ABSTRACT = 'Show Abstract (classes)'
    FILTER_ACROSS_ARCS = 'Filter Across Arcs'

    ContextMenuHierarchy = actions.HierarchyStandardContextMenuStrategy

    def __init__(self, parent=None):
        super(HierarchyEditor, self).__init__(parent=parent)

        self._menu_bar = QMenuBar()
        self._show_menu = QMenu('Show')
        self._menu_bar.addMenu(self._show_menu)
        self._filter_line_edit = QLineEdit()
        self._hierarchy_view = QTreeView()
        self._show_menu_items = OrderedDict(
            [
                (HierarchyEditor.SHOW_INACTIVE, QAction(HierarchyEditor.SHOW_INACTIVE, self)),
                (HierarchyEditor.SHOW_UNDEFINED, QAction(HierarchyEditor.SHOW_UNDEFINED, self)),
                (HierarchyEditor.SHOW_ABSTRACT, QAction(HierarchyEditor.SHOW_ABSTRACT, self)),
                (HierarchyEditor.FILTER_ACROSS_ARCS, QAction(HierarchyEditor.FILTER_ACROSS_ARCS, self))
            ]
        )

        for item in self._show_menu_items:
            self._show_menu_items[item].setCheckable(True)
            self._show_menu.addAction(self._show_menu_items[item])

        self._filter_model = hierarchyModel.HierarchyStandardFilterModel()

        self._show_menu_items[HierarchyEditor.SHOW_INACTIVE].toggled.connect(self._filter_model.TogglePrimInactive)
        self._show_menu_items[HierarchyEditor.SHOW_UNDEFINED].toggled.connect(self._filter_model.TogglePrimUndefined)
        self._show_menu_items[HierarchyEditor.SHOW_ABSTRACT].toggled.connect(self._filter_model.TogglePrimAbstract)
        self._show_menu_items[HierarchyEditor.FILTER_ACROSS_ARCS].toggled.connect(
            self._filter_model.ToggleFilterAcrossArcs)

        self._show_menu_items[HierarchyEditor.SHOW_INACTIVE].setChecked(False)
        self._show_menu_items[HierarchyEditor.SHOW_UNDEFINED].setChecked(False)
        self._show_menu_items[HierarchyEditor.SHOW_ABSTRACT].setChecked(False)
        self._show_menu_items[HierarchyEditor.FILTER_ACROSS_ARCS].setChecked(True)

        self._layout = QVBoxLayout(self)
        self.setLayout(self._layout)
        self._layout.addWidget(self._menu_bar)
        self._layout.addWidget(self._filter_line_edit)
        self._layout.addWidget(self._hierarchy_view)

        self._hierarchy_view.setModel(self._filter_model)
        self._hierarchy_view.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self._filter_line_edit.returnPressed.connect(self._on_filter_return_pressed)

        self._setup_context_menu()

    @property
    def primSelectionChanged(self):
        """
        Provides access to the internal QItemSelectionModel's selectionChanged signal for callbacks
        on prim selection changes
        """

        return self._hierarchy_view.selectionModel().selectionChanged

    def select_paths(self, paths):
        item_selection = QItemSelection()
        source_model = self._filter_model.sourceModel()
        for path in paths:
            index = source_model.GetIndexFromPath(path)
            if index and index.isValid():
                item_selection.select(index, index)
        mapped_selection = self._filter_model.mapSelectionFromSource(item_selection)
        self._hierarchy_view.selectionModel().select(mapped_selection, QItemSelectionModel.ClearAndSelect)

    def get_selected_prims(self):
        selected_indices = self._hierarchy_view.selectedIndexes()
        ordered_prims = list()
        unordered_prims = set()
        for index in selected_indices:
            prim = index.data(role=roles.HierarchyPrimRole)
            if prim not in unordered_prims:
                unordered_prims.add(prim)
                ordered_prims.append(prim)

        return ordered_prims

    def set_source_model(self, model):
        self._filter_model.setSourceModel(model)

    def _setup_context_menu(self):
        self._context_menu = self.ContextMenuHierarchy(self)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._context_menu.construct)

    def _on_filter_return_pressed(self):
        self._filter_model.SetPathContainsFilter(self._filter_line_edit.text())


class HierarchyEditorListener(QObject, object):
    def __init__(self, parent=None):
        super(HierarchyEditorListener, self).__init__(parent=parent)

    def OnPrimSelectionChanged(self, selected=None, deselected=None):
        for index in self.sender().selectedIndexes():
            prim = index.data(role=roles.HierarchyPrimRole)
