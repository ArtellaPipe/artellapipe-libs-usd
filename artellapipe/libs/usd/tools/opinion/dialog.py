#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Opinion Editor dialog implementations
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging

import tpDcc as tp

from pxr.UsdQt import opinionModel

from artellapipe.libs.usd.tools.opinion import editor

LOGGER = logging.getLogger('artellapipe-libs-usd')


class OpinionEditorDialog(tp.Dialog, object):
    def __init__(self, stage, prims, *args, **kwargs):

        self._stage = stage
        self._model = opinionModel.OpinionStandardModel(prims)

        kwargs['title'] = 'USD - Opinion Editor'
        super(OpinionEditorDialog, self).__init__(*args, **kwargs)

        self._editor = editor.OpinionEditor()
        self._controller = editor.OpinionController(self._model, self._editor)
        self._editor.set_source_model(self._model)

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
        prim = list(current_stage.TraverseAll())[0]

        return cls(stage=current_stage, prims=[prim], parent=parent)


def run(parent=None):
    dialog = OpinionEditorDialog.from_current_scene(parent=parent)
    if dialog:
        dialog.show()

    return dialog
