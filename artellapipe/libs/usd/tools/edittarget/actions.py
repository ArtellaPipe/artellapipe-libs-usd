#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USD Edit Target actions implementation
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from Qt.QtWidgets import *
from Qt.QtGui import *

from artellapipe.libs.usd.core import usdqtutils
from artellapipe.libs.usd.tools.layertext import dialog


class ShowLayerText(usdqtutils.MenuAction, object):

    DEFAULT_TEXT = 'Show Layer Text'

    def do(self):
        context = self.get_current_context()
        if not context.selected_layer:
            return

        qt_parent = context.qt_parent
        if qt_parent and hasattr(qt_parent, 'show_layer_text_dialog'):
            qt_parent.show_layer_text_dialog(context.selected_layer)
        else:
            layer_text_dialog = dialog.LayerTextEditorDialog.get_shared_instance(
                context.selected_layer, parent=qt_parent or context.layer_dialog)
            layer_text_dialog.show()
            layer_text_dialog.raise_()
            layer_text_dialog.activateWindow()


class CopyLayerPath(usdqtutils.MenuAction, object):

    DEFAULT_TEXT = 'Copy Layer Identifier'

    def do(self):
        context = self.get_current_context()
        if context.selected_layer:
            text = context.selected_layer.identifier
            clipboard = QApplication.clipboard()
            clipboard.setText(text. QClipboard.Selection)
            clipboard.setText(text, QClipboard.Clipboard)


class OpenLayer(usdqtutils.MenuAction, object):

    DEFAULT_TEXT = 'Open Layer in Outliner'

    def do(self):
        context = self.get_current_context()
        if context.selected_layer:
            raise NotImplementedError
