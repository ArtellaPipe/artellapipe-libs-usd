#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Layer Text Editor widget implementations
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from Qt.QtCore import *
from Qt.QtWidgets import *

from pxr import Sdf, Tf


class LayerTextEditor(QWidget, object):
    layerSaved = Signal(Sdf.Layer)

    def __init__(self, layer, read_only=False, parent=None):
        super(LayerTextEditor, self).__init__(parent=parent)

        self._layer = layer
        self._read_only = read_only

        self._text_area = QPlainTextEdit(self)
        refresh_button = QPushButton('Reload', parent=self)
        refresh_button.clicked.connect(self.refresh)

        layout = QVBoxLayout(self)
        self.setLayout(layout)
        button_layout = QHBoxLayout()
        button_layout.addWidget(refresh_button)

        if not read_only:
            editable_check = QCheckBox('Unlock for editing', parent=self)
            editable_check.setChecked(False)
            editable_check.stateChanged.connect(self.set_editable)
            layout.addWidget(editable_check)
            self._save_button = QPushButton('Apply', parent=self)
            self._save_button.clicked.connect(self.save)
            button_layout.addWidget(self._save_button)

        layout.addWidget(self._text_area)
        layout.addLayout(button_layout)

        self.set_editable(False)
        self.refresh()

    @property
    def read_only(self):
        return self._read_only

    def set_editable(self, flag):
        if flag:
            if self.read_only:
                return
            self._text_area.setUndoRedoEnabled(True)
            self._text_area.setReadOnly(False)
            self._save_button.setEnabled(True)
        else:
            self._text_area.setUndoRedoEnabled(False)
            self._text_area.setReadOnly(True)
            if not self._read_only:
                self._save_button.setEnabled(False)

    def refresh(self):
        self._text_area.setPlainText(self._layer.ExportToString())

    def save(self):
        if self._read_only:
            raise RuntimeError('Cannot save layer when read_only is set')

        try:
            success = self._layer.ImportFromString(self._text_area.toPlainText())
        except Tf.ErrorException as exc:
            QMessageBox.warning(
                self, 'Layer Syntax Error', 'Failed to apply modifed layer contents:\n\n{}'.format(exc.message))
        else:
            if success:
                self.layerSaved.emit(self._layer)
                self.refresh()
