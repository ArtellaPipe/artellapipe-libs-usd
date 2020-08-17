#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Layer Text Editor dialog implementations
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from Qt.QtWidgets import *

from artellapipe.libs.usd.tools.layertext import editor


class LayerTextEditorDialog(QDialog, object):

    _sharedInstances = dict()

    def __init__(self, layer, read_only=False, parent=False):
        super(LayerTextEditorDialog, self).__init__(parent=parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self._editor = editor.LayerTextEditor(layer, read_only=read_only, parent=self)
        layout.addWidget(self._editor)

        self.setWindowTitle('Layer: {}'.format(layer.identifier))
        self.resize(800, 600)

    @property
    def editor(self):
        return self._editor

    @classmethod
    def _on_shared_instance_finished(cls, layer):
        dialog = cls._sharedInstances.pop(layer, None)
        if dialog:
            dialog.deleteLater()

    @classmethod
    def get_shared_instance(cls, layer, read_only=False, parent=None):
        dialog = cls._sharedInstances.get(layer, None)
        if not dialog:
            dialog = cls(layer, read_only=read_only, parent=parent)
            cls._sharedInstances[layer] = dialog
            dialog.finished.connect(lambda result: cls._on_shared_instance_finished(layer))

        return dialog
