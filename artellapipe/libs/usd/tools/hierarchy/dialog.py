#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Hierarchy Editor dialog implementations
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging

from pxr.UsdQt import hierarchyModel

import tpDcc as tp

from artellapipe.libs.usd.tools.hierarchy import editor

LOGGER = logging.getLogger('artellapipe-libs-usd')


class HierarchyEditorDialog(tp.Dialog, object):
    def __init__(self, stage, *args, **kwargs):

        self._stage = stage
        self._model = hierarchyModel.HierarchyBaseModel(stage)

        kwargs['title'] = 'USD - Hierarchy Editor'
        super(HierarchyEditorDialog, self).__init__(*args, **kwargs)

        self._editor = editor.HierarchyEditor()
        self._editor.set_source_model(self._model)
        self._listener = editor.HierarchyEditorListener()
        self._editor.primSelectionChanged.connect(self._listener.OnPrimSelectionChanged)

        self.main_layout.addWidget(self._editor)

    @classmethod
    def from_current_scene(cls, parent=None):
        import mayaUsd.lib as mayaUsdLib
        stage_cache = mayaUsdLib.StageCache.Get(True)
        if not stage_cache:
            LOGGER.warning('No USD stage cache found in current scene!')
            return

        all_stages = stage_cache.GetAllStages()
        if not all_stages:
            LOGGER.warning('No USD cache found in current scene!')
            return

        current_stage = all_stages[0]

        return cls(stage=current_stage, parent=parent)


def run(parent=None):
    dialog = HierarchyEditorDialog.from_current_scene(parent=parent)
    if dialog:
        dialog.show()

    return dialog
