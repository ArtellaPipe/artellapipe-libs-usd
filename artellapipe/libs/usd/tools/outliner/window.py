#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD outliner window implementation
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging

from Qt.QtCore import *

from pxr import Sdf, Tf, Usd

import tpDcc

from artellapipe.libs.usd.tools.outliner.widgets import outliner

LOGGER = logging.getLogger('artellapipe-libs-usd')


class UsdOutlinerWindow(tpDcc.Window, object):

    stageChanged = Signal(object)

    def __init__(self, stage, role=None, *args, **kwargs):

        self._role = role
        self._stage = stage
        self._listener = None

        super(UsdOutlinerWindow, self).__init__(*args, **kwargs)

    def ui(self):
        super(UsdOutlinerWindow, self).ui()

        self.reset_stage(self._stage)

        self._outliner = outliner.UsdOutliner(self._stage, role=self._role, parent=self)
        self.main_layout.addWidget(self._outliner)

        self.resize(900, 600)

    def setup_signals(self):
        super(UsdOutlinerWindow, self).setup_signals()

        self.stageChanged.connect(self._outliner.reset_stage)

    @classmethod
    def from_current_scene(cls, role=None, parent=None):
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

        return cls(current_stage, role=role, parent=parent)

    def closeEvent(self, event):
        self.reset_stage()

    def reset_stage(self, stage=None):
        if stage:
            self._listener = Tf.Notice.Register(Usd.Notice.StageEditTargetChanged, self._on_edit_target_changed, stage)
        else:
            if self._listener:
                self._listener.Revoke()
            self._listener = None

        self._stage = stage

        self._update_title()
        self.stageChanged.emit(stage)

    def _update_title(self, identifier=None):
        if not identifier and self._stage:
            identifier = self._stage.GetEditTarget().GetLayer().identifier
        self.setWindowTitle('Outliner - {}'.format(identifier))

    def _on_edit_target_changed(self, notice, stage):
        self._update_title()


def run(role=None, parent=None):
    window = UsdOutlinerWindow.from_current_scene(role=role, parent=parent)
    if window:
        window.show()

    return window
