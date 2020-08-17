#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Edit Target Editor widget implementations
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from collections import namedtuple

from Qt.QtWidgets import *

from artellapipe.libs.usd.tools.edittarget import treeview


LayerStackDialogContext = namedtuple(
    'LayerStackDialogContext', ['qt_parent', 'layer_dialog', 'stage', 'selected_layer', 'edit_target_layer'])


class EditTargetEditor(QWidget, object):
    def __init__(self, stage, edit_target_change_callback=None, parent=None):
        super(EditTargetEditor, self).__init__(parent=parent)

        self._stage = stage
        self._data_model = treeview.LayerStackModel(stage, parent=self)
        self._edit_target_change_callback = edit_target_change_callback

        self._view = treeview.LayerStackTreeView(self, parent=self)
        self._view.setModel(self._data_model)
        self._view.doubleClicked.connect(self.change_edit_target)
        self._view.setColumnWidth(0, 160)
        self._view.setColumnWidth(1, 300)
        self._view.setColumnWidth(2, 100)
        self._view.setExpandsOnDoubleClick(False)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(4, 4, 4, 4)
        main_layout.setSpacing(2)
        self.setLayout(main_layout)
        main_layout.addWidget(self._view)

        self._view.expandAll()

    def get_menu_context(self):
        stage = self._stage
        return LayerStackDialogContext(
            qt_parent=self.parent() or self, layer_dialog=self, stage=stage,
            selected_layer=self._view.get_selected_layer(), edit_target_layer=stage.GetEditTarget().GetLayer())

    def change_edit_target(self, model_index):
        if not model_index.isValid():
            return

        item = model_index.internalPointer()
        new_layer = item.layer

        if self._edit_target_change_callback is None or self._edit_target_change_callback(new_layer):
            self._stage.SetEditTarget(new_layer)

    def reset_stage(self, stage):
        self._data_model.ResetStage(stage)
        self._stage = stage
