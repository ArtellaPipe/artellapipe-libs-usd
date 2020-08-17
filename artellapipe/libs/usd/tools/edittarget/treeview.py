#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Edit Target Editor tree view implementations
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from Qt.QtCore import *
from Qt.QtWidgets import *
from Qt.QtGui import *

from pxr import Tf, Usd
from pxr.UsdQt import layerModel

from artellapipe.libs.usd.core import usdqtutils
from artellapipe.libs.usd.tools.edittarget import actions

FONT_BOLD = QFont()
FONT_BOLD.setBold(True)
NULL_INDEX = QModelIndex()


class LayerStackModel(layerModel.LayerStackBaseModel, object):

    headerLabels = ('Name', 'Path', 'Resolved Path')

    def __init__(self, stage, include_session_layers=True, parent=None):
        super(LayerStackModel, self).__init__(stage, includeSessionLayers=include_session_layers, parent=parent)

        self._listener = Tf.Notice.Register(Usd.Notice.StageEditTargetChanged, self._on_edit_target_changed, stage)

    def columnCount(self, parent_index):
        return 3

    def flags(self, model_index):
        if model_index.isValid():
            item = model_index.internalPointer()
            if item.layer.permissionToEdit:
                return Qt.ItemIsEnabled | Qt.ItemIsSelectable

        return Qt.NoItemFlags

    def data(self, model_index, role=Qt.DisplayRole):
        if not model_index.isValid():
            return

        if role == Qt.DisplayRole:
            column = model_index.column()
            item = model_index.internalPointer()
            if column == 0:
                if item.layer.anonymous:
                    return '<anonymous>'
                return item.layer.identifier.split('/')[-1]
            elif column == 1:
                return item.layer.identifier
            elif column == 2:
                return item.layer.realPath
        elif role == Qt.FontRole:
            item = model_index.internalPointer()
            if item.layer == self._stage.GetEditTarget().GetLayer():
                return FONT_BOLD

    def ResetStage(self, stage):
        super(LayerStackModel, self).ResetStage(stage)
        if self._stage:
            self._listener = Tf.Notice.Register(Usd.Notice.StageEditTargetChanged, self._on_edit_target_changed, stage)
        else:
            self._listener = None

    def _on_edit_target_changed(self, notice, stage):
        self.dataChanged.emit(NULL_INDEX, NULL_INDEX)


class LayerStackTreeView(usdqtutils.ContextMenuMixin, QTreeView):
    def __init__(self, context_provider, parent=None):

        context_menu_actions = [actions.ShowLayerText, actions.CopyLayerPath, actions.OpenLayer]

        super(LayerStackTreeView, self).__init__(
            context_menu_actions=context_menu_actions, context_provider=context_provider, parent=parent)

    def get_selected_layer(self):
        selection_model = self.selectionModel()
        indexes = selection_model.selectedRows()
        if indexes:
            index = indexes[0]
            if index.isValid():
                return index.internalPointer().layer
