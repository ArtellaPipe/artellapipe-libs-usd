#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD outliner widget implementations
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from collections import namedtuple

from Qt.QtCore import *
from Qt.QtWidgets import *

from pxr import Sdf, Tf, Usd
from pxr.UsdQt import hierarchyModel

from artellapipe.libs.usd.core import usdqtutils
from artellapipe.libs.usd.tools.outliner import actions
from artellapipe.libs.usd.tools.outliner.widgets import treeview
from artellapipe.libs.usd.tools.edittarget import dialog as edittargetdialog
from artellapipe.libs.usd.tools.layertext import dialog as layertextdialog


OutlinerContext = namedtuple(
    'OutlinerContext', ['qt_parent', 'outliner', 'stage', 'edit_target_layer', 'selected_prim', 'selected_prims'])


class UsdOutliner(QWidget, object):

    stageChanged = Signal(Usd.Stage)

    def __init__(self, stage, role=None, parent=None):
        super(UsdOutliner, self).__init__(parent=parent)

        self._stage = None
        self._listener = None
        self._shared_layer_text_editors = dict()
        self._edit_target_dialog = None
        self._variant_editor_dialog = None
        self._data_model = hierarchyModel.HierarchyBaseModel(stage=stage, parent=self)
        self._role = role or actions.OutlinerRole
        self.reset_stage(stage)

        view = self._create_view(self._role)
        view.setColumnWidth(0, 360)
        view.setModel(self._data_model)
        self._view = view

        delegate = treeview.OutlinerViewDelegate(stage, parent=self)
        view.setItemDelegate(delegate)
        self.stageChanged.connect(delegate.reset_stage)

        self._menu_bar_builder = usdqtutils.MenuBarBuilder(
            self, menu_builders=self._role.get_menu_bar_menu_builders(self), parent=self)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(4, 4, 4, 4)
        main_layout.setSpacing(2)
        self.setLayout(main_layout)
        main_layout.addWidget(view)

    @property
    def stage(self):
        return self._stage

    def get_menu_context(self):
        selected_prims = self._view.selected_prims()
        selected_prim = selected_prims[0] if selected_prims else None
        return OutlinerContext(
            qt_parent=self, outliner=self, stage=self._stage, edit_target_layer=self.get_edit_target_layer(),
            selected_prim=selected_prim, selected_prims=selected_prims)

    def get_edit_target_layer(self):
        if not self._stage:
            return None

        return self._stage.GetEditTarget().GetLayer()

    def reset_stage(self, stage):
        self._stage = stage
        self._data_model.ResetStage(stage)
        self.stageChanged.emit(stage)

    def show_layer_text_dialog(self, layer=None):
        layer = layer or self.get_edit_target_layer()
        dialog = self._get_shared_layer_text_editor_instance(layer)
        self.stageChanged.connect(dialog.close)
        dialog.show()
        dialog.raise_()
        dialog.activateWindow()

    def show_edit_target_layer_dialog(self):
        if not self._edit_target_dialog:
            dialog = edittargetdialog.EditTargetDialog(
                self._stage, edit_target_change_callback=self._on_layer_dialog_edit_target_change_callback, parent=self)
            self.stageChanged.connect(dialog.editor.reset_stage)
            self._edit_target_dialog = dialog
        self._edit_target_dialog.show()
        self._edit_target_dialog.raise_()
        self._edit_target_dialog.activateWindow()

    def _create_view(self, role):
        return treeview.OutlinerTreeView(
            context_menu_actions=role.get_context_menu_actions(self), context_provider=self, parent=self)

    def _get_shared_layer_text_editor_instance(self, layer):
        dialog = self._shared_layer_text_editors.get(layer, None)
        if dialog is None:
            read_only = not layer.permissionToEdit
            dialog = layertextdialog.LayerTextEditorDialog(layer, read_only=read_only, parent=self)
            self._shared_layer_text_editors[layer] = dialog
            dialog.finished.connect(lambda result: self._on_layer_text_editor_finished(layer))

        return dialog

    def _on_layer_text_editor_finished(self, layer):
        dialog = self._shared_layer_text_editors.pop(layer, None)
        if dialog:
            dialog.deleteLater()

    def _on_layer_dialog_edit_target_change_callback(self, new_layer):
        current_layer = self.get_edit_target_layer()
        if new_layer == current_layer or not new_layer.permissionToEdit:
            return False

        if current_layer.dirty:
            box = QMessageBox(
                QMessageBox.Warning,
                'Unsaved Layer Changes',
                'The current edit target layer contains unsaved edits which will not be accessible after changing '
                'edit targets. Are you sure you want to switch?', buttons=QMessageBox.No | QMessageBox.Yes, parent=self)
            if box.exec_() != QMessageBox.Yes:
                return False

        return True
