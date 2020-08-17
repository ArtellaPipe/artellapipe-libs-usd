#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Outliner role actions
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import difflib
from functools import partial

from Qt.QtWidgets import *

from pxr import Sdf, Tf, Usd
from pxr.UsdQt import hooks

from artellapipe.libs.usd.core import usdutils, usdqtutils

NO_VARIANT_SELECTION = '<No Variant Selection>'


class OutlinerRole(object):

    @classmethod
    def get_context_menu_actions(cls, outliner):
        return [ActivatePrims, DeactivatePrims, SelectVariants, usdqtutils.MenuSeparator,
                AddTransform, AddReference, usdqtutils.MenuSeparator, RemovePrim]

    @classmethod
    def get_menu_bar_menu_builders(cls, outliner):
        save_state = SaveState(outliner)
        return [usdqtutils.MenuBuilder('&File', [SaveEditLayer(save_state)]),
                usdqtutils.MenuBuilder('&Tools', [ShowEditTargetLayerText, ShowEditTargetDialog])]


class SaveState(object):
    def __init__(self, outliner):
        super(SaveState, self).__init__()

        self._outliner = outliner
        edit_target = outliner.get_edit_target_layer()
        self._orig_layer_contents = {self.get_id(edit_target): self._get_disk_contents(edit_target)}
        self._listener = Tf.Notice.Register(
            Usd.Notice.StageEditTargetChanged, self._on_edit_target_changed, outliner.stage)

    def get_id(self, layer):
        return hooks.UsdQtHooks.Call('GetId', layer)

    def get_original_contents(self, layer):
        return self._orig_layer_contents[self.get_id(layer)]

    def save_original_contents(self, layer, contents=None):
        if not contents:
            contents = layer.ExportToString()
        self._orig_layer_contents[self.get_id(layer)] = contents

    def check_original_contents(self, layer):
        disk_contents = self._get_disk_contents(layer)
        original_contents = self.get_original_contents(layer)
        if original_contents and original_contents != disk_contents:
            diff = difflib.unified_diff(original_contents.split('\n'), disk_contents.split('\n'),
                                        fromfile='original', tofile='on disk', n=10)
            dlg = QMessageBox(
                QMessageBox.Warning,
                'Layer Contents Changed!',
                'Layer contents have changed on disk since you started editing.\n       '
                '{}\nSave anyway and risk overwriting changes?'.format(layer.identifier),
                buttons=QMessageBox.No | QMessageBox.Yes, detailedText='\n'.join(diff))
            if dlg.exec_() != QMessageBox.Yes:
                return False

        return True

    def _get_disk_contents(self, layer):
        if not layer.realPath:
            return None

        # TODO: Is it safe to ChangeBlock this content swapping?
        current_contents = layer.ExportToString()
        layer.Reload()
        disk_contents = layer.ExportToString()
        if disk_contents != current_contents:
            layer.ImportFromString(current_contents)

        return disk_contents

    def _on_edit_target_changed(self, notice, stage):
        layer = stage.GetEditTarget().GetLayer()
        self._orig_layer_contents.setdefault(self.get_id(layer), layer.ExportToString())


class SaveEditLayer(usdqtutils.MenuAction, object):

    DEFAULT_TEXT = 'Save Current Edit Layer'

    def __init__(self, state):
        super(SaveEditLayer, self).__init__()

        self._state = state

    def do(self):
        context = self.get_current_context()
        edit_target = context.edit_target_layer
        if not edit_target.dirty:
            print('Nothing to save')
            return
        if not self._state.check_original_contents(edit_target):
            return

        self._save_layer(edit_target)

    def _save_layer(self, layer):
        layer.Save()
        self._state.save_original_contents(layer)


def run():
    from artellapipe.libs.usd.tools.outliner import window
    window = window.UsdOutlinerWindow.from_current_scene()
    if window:
        window.show()


class ShowEditTargetLayerText(usdqtutils.MenuAction, object):
    DEFAULT_TEXT = 'Show Current Layer Text'

    def do(self):
        context = self.get_current_context()
        context.outliner.show_layer_text_dialog()


class ShowEditTargetDialog(usdqtutils.MenuAction, object):
    DEFAULT_TEXT = 'Change Edit Target'

    def do(self):
        context = self.get_current_context()
        context.outliner.show_edit_target_layer_dialog()


class ActivatePrims(usdqtutils.MenuAction, object):

    DEFAULT_TEXT = 'Activate'

    def update(self, action, context):
        action.setEnabled(bool(context.selected_prims))

    def do(self):
        context = self.get_current_context()
        with Sdf.ChangeBlock():
            for prim in context.selected_prims:
                prim.SetActive(True)


class DeactivatePrims(usdqtutils.MenuAction, object):

    DEFAULT_TEXT = 'Deactivate'

    def update(self, action, context):
        action.setEnabled(bool(context.selected_prims))

    def do(self):
        context = self.get_current_context()
        with Sdf.ChangeBlock():
            for prim in context.selected_prims:
                prim.SetActive(False)


class SelectVariants(usdqtutils.MenuAction, object):

    def build(self, context):
        prims = context.selected_prims
        if len(prims) != 1:
            return
        prim = prims[0]
        if not prim.HasVariantSets():
            return

        menu = QMenu('Variants', context.qt_parent)
        for set_name, current_value in usdutils.get_prim_variants(prim):
            set_menu = menu.addMenu(set_name)
            variant_set = prim.GetVariantSet(set_name)
            for set_value in [NO_VARIANT_SELECTION] + variant_set.GetVariantNames():
                new_action = set_menu.addAction(set_value)
                new_action.setCheckable(True)
                if set_value == current_value or (set_value == NO_VARIANT_SELECTION and current_value == ''):
                    new_action.setChecked(True)
                new_action.triggered.connect(partial(self._apply_variant, prim, set_name, set_value))

        return menu.menuAction()

    @staticmethod
    def _apply_variant(prim, variant_set_name, variant_value):
        if prim:
            variant_set = prim.GetVariantSet(variant_set_name)
            if variant_value == NO_VARIANT_SELECTION:
                variant_set.ClearVariantSelection()
            else:
                variant_set.SetVariantSelection(variant_value)


class AddReference(usdqtutils.MenuAction, object):

    DEFAULT_TEXT = 'Add Reference...'

    def update(self, action, context):
        context = self.get_current_context()
        action.setEnabled(bool(context.selected_prim))

    def do(self):
        context = self.get_current_context()
        ref_path = hooks.UsdQtHooks.Call('GetReferencePath', stage=context.stage)
        if ref_path:
            stage = context.stage
            prim = context.selected_prim
            edit_layer = context.edit_target_layer
            if not stage.HasLocalLayer(edit_layer):
                edit_target_stage = Usd.Stage.Open(edit_layer)
                prim = edit_target_stage.GetPrimAtPath(prim.GetPath())

            prim.GetReferences().SetReferences([Sdf.Reference(ref_path)])


class AddTransform(usdqtutils.MenuAction, object):

    DEFAULT_TEXT = 'Add Transform ...'

    def update(self, action, context):
        action.setEnabled(bool(context.selected_prim))

    def do(self):
        context = self.get_current_context()

        # TODO: Right now this only produces Xforms. May need to support the ability to specify types for new prims.
        name, _ = QInputDialog.getText(context.qt_parent, 'Add New Transform', 'Transform Name: ')
        if not name:
            return

        if not Sdf.Path.IsValidIdentifier(name):
            QMessageBox.warning(context.qt_parente, 'Invalid Prim Name', '{0!r} is not a valid prim name'.format(name))
            return

        new_path = context.selected_prim.GetPath().AppendChild(name)
        if context.stage.GetEditTarget().GetPrimSpecForScenePath(new_path):
            QMessageBox.warning(
                context.qt_parent, 'Duplicate Prim Path', 'A prim already exists at {0!r,}'.format(new_path))
            return

        context.stage.DefinePrim(new_path, 'Xform')


class RemovePrim(usdqtutils.MenuAction, object):

    def update(self, action, context):
        prims = context.selected_prims
        action.setEnabled(bool(prims))
        text = 'Remove Prims' if len(prims) > 1 else 'Remove Prim'
        edit_target = context.stage.GetEditTarget()
        for prim in prims:
            spec = edit_target.GetPrimSpecForScenePath(prim.GetPath())
            if spec and spec.specifier == Sdf.SpecifierOver:
                text = 'Remove Prim Edits'
                break
        action.setText(text)

    def do(self):
        context = self.get_current_context()
        ask = True
        buttons = QMessageBox.Yes | QMessageBox.Cancel
        if len(context.selected_prims) > 1:
            buttons |= QMessageBox.YesToAll

        for prim in context.selected_prims:
            prim_path = prim.GetPath()
            if ask:
                answer = QMessageBox.question(
                    context.qt_parent,
                    'Confirm Prim Deletion',
                    'Remove prim/prim edits (and any children) at {}?'.format(
                        prim_path), buttons=buttons, defaultButton=QMessageBox.Yes)
                if answer == QMessageBox.Cancel:
                    return
                elif answer == QMessageBox.YesToAll:
                    ask = False
            context.stage.RemovePrim(prim_path)
