#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Outliner tree view implementation
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from Qt.QtCore import *
from Qt.QtWidgets import *
from Qt.QtGui import *

from pxr import Sdf, Tf, Usd

from tpDcc.libs.qt.core import color

from artellapipe.libs.usd.core import usdqtutils


class OutlinerTreeView(usdqtutils.ContextMenuMixin, QTreeView):

    primSelectionChanged = Signal(list, list)

    def __init__(self, context_menu_actions, context_provider=None, parent=None):
        super(OutlinerTreeView, self).__init__(
            context_menu_actions=context_menu_actions, context_provider=context_provider, parent=parent)

        self._data_model = None

        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.ExtendedSelection)
        self.setEditTriggers(self.CurrentChanged | self.SelectedClicked)
        self.setUniformRowHeights(True)
        self.header().setStretchLastSection(True)

    def setModel(self, model):
        if model == self._data_model:
            return

        old_selection_model = self.selectionModel()
        super(OutlinerTreeView, self).setModel(model)
        self._data_model = model

        # This can't be a one-liner because of a PySide refcount bug.
        selection_model = self.selectionModel()
        selection_model.selectionChanged.connect(self._on_selection_changed)
        if old_selection_model:
            old_selection_model.deleteLater()

    def selected_prims(self):
        model = self._data_model
        result = list()
        for index in self.selectionModel().selectedRows():
            prim = model._GetPrimForIndex(index)
            if prim:
                result.append(prim)

        return result

    def _on_selection_changed(self, selected, deselected):
        model = self._data_model

        def _to_prims(selection):
            return [model._GetPrimForIndex(index) for index in selection.indexes() if index.column() == 0]

        self.primSelectionChanged.emit(_to_prims(selected), _to_prims(deselected))


class OutlinerViewDelegate(QStyledItemDelegate, object):
    def __init__(self, stage, parent=None):
        super(OutlinerViewDelegate, self).__init__(parent=parent)

        self._active_layer = None
        self._listener = None
        self.reset_stage(stage)

    def paint(self, painter, options, model_index):
        if not model_index.isValid():
            return super(OutlinerViewDelegate, self).paint(painter, options, model_index)

        proxy = model_index.internalPointer()
        if not proxy.expired:
            prim = proxy.GetPrim()
            palette = options.palette
            text_color = palette.color(QPalette.Text)
            if prim.HasVariantSets():
                text_color = color.DARK_ORANGE
            if not prim.IsActive():
                text_color.setAlphaF(0.5)
            spec = self._active_layer.GetPrimAtPath(prim.GetPrimPath())
            if spec:
                specifier = spec.specifier
                if specifier == Sdf.SpecifierDef:
                    options.font.setBold(True)
                elif specifier == Sdf.SpecifierOver:
                    options.font.setItalic(True)
            palette.setColor(QPalette.Text, text_color)

        return super(OutlinerViewDelegate, self).paint(painter, options, model_index)

    def set_active_layer(self, layer):
        self._active_layer = layer

    def reset_stage(self, stage):
        if stage:
            self._active_layer = stage.GetEditTarget().GetLayer()
            self._listener = Tf.Notice.Register(Usd.Notice.StageEditTargetChanged, self._on_edit_target_changed, stage)
        else:
            self._listener = None
            self._active_layer = None

    def _on_edit_target_changed(self, notice, stage):
        self.set_active_layer(stage.GetEditTarget().GetLayer())
