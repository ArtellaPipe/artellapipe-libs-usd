#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Hierarchy Editor actions implementations
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from collections import defaultdict

from Qt.QtWidgets import *

from pxr import Sdf


class HierarchyStandardContextMenuStrategy(object):
    def __init__(self, hierarchy_editor):
        self._hierarchy_editor = hierarchy_editor

    def construct(self, point):
        prims = self._get_selected_prims()
        if len(prims) == 1:
            name = prims[0].GetName()
        else:
            name = '{} selected prims'.format(len(prims))

        menu = QMenu()
        activate_action = menu.addAction('Activate {}'.format(name))
        deactivate_action = menu.addAction('Deactivate {}'.format(name))
        clear_activate_action = menu.addAction('Clear Activation for {}'.format(name))
        load_action = menu.addAction('Load {}'.format(name))
        unload_action = menu.addAction('Unload {}'.format(name))

        activate_action.triggered.connect(self.activate_selection)
        deactivate_action.triggered.connect(self.deactivate_selection)
        clear_activate_action.triggered.connect(self.clear_active_for_selection)
        load_action.triggered.connect(self.load_selection)
        unload_action.triggered.connect(self.unload_selection)

        menu.exec_(self._hierarchy_editor.mapToGlobal(point))

    def activate_selection(self):
        with Sdf.ChangeBlock():
            prims = self._get_selected_prims()
            for prim in prims:
                prim.SetActive(True)

    def deactivate_selection(self):
        with Sdf.ChangeBlock():
            prims = self._get_selected_prims()
            for prim in prims:
                prim.SetActive(False)

    def clear_active_for_selection(self):
        with Sdf.ChangeBlock():
            prims = self._get_selected_prims()
            for prim in prims:
                prim.ClearActive()

    def load_selection(self):
        prims = self._get_selected_prims()
        stage_map = self._build_stage_map(prims)
        for stage in stage_map:
            stage.LoadAndUnload(stage_map[stage], [])

    def unload_selection(self):
        prims = self._get_selected_prims()
        stage_map = self._build_stage_map(prims)
        for stage in stage_map:
            stage.LoadAndUnload([], stage_map[stage])

    def _get_selected_prims(self):
        selection = self._hierarchy_editor.get_selected_prims()
        selection.sort(key=lambda prim: prim.GetPath(), reverse=True)

        return selection

    def _build_stage_map(self, prims):
        """
        Internal function that allow to support hibrid models (altough usually all prims belong to same stage, we need
        to support the opposite scenario).
        :param prims: list(Usd.Prim)
        :return:dict(Usd.Stage, set(Sdf.Path))
        """

        stage_map = defaultdict(set)
        for prim in prims:
            stage_map[prim.GetStage()].add(prim.GetPath())

        return stage_map
