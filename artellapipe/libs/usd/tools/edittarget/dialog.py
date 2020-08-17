#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Edit Target Editor dialog implementations
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from Qt.QtWidgets import *

from artellapipe.libs.usd.tools.edittarget import editor


class EditTargetDialog(QDialog, object):
    def __init__(self, stage, edit_target_change_callback=None, parent=None):
        super(EditTargetDialog, self).__init__(parent=parent)

        self.setWindowTitle('Select Edit Target')
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)
        self._editor = editor.EditTargetEditor(
            stage, edit_target_change_callback=edit_target_change_callback, parent=self)
        main_layout.addWidget(self._editor)
        self.resize(700, 200)

    @property
    def editor(self):
        return self._editor
