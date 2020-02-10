# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/usd/pixar_usd/USD/pxr/usdImaging/usdviewq/attributeValueEditorUI.ui'
#
# Created: Sat Feb  1 02:03:31 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AttributeValueEditor(object):
    def setupUi(self, AttributeValueEditor):
        AttributeValueEditor.setObjectName("AttributeValueEditor")
        AttributeValueEditor.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(AttributeValueEditor)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtGui.QStackedWidget(AttributeValueEditor)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.valueViewer = QtGui.QTextBrowser()
        self.valueViewer.setObjectName("valueViewer")
        self.stackedWidget.addWidget(self.valueViewer)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(AttributeValueEditor)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AttributeValueEditor)

    def retranslateUi(self, AttributeValueEditor):
        AttributeValueEditor.setWindowTitle(QtGui.QApplication.translate("AttributeValueEditor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        AttributeValueEditor.setProperty("comment", QtGui.QApplication.translate("AttributeValueEditor", "\n"
"     Copyright 2016 Pixar                                                                   \n"
"                                                                                            \n"
"     Licensed under the Apache License, Version 2.0 (the \"Apache License\")      \n"
"     with the following modification; you may not use this file except in                   \n"
"     compliance with the Apache License and the following modification to it:               \n"
"     Section 6. Trademarks. is deleted and replaced with:                                   \n"
"                                                                                            \n"
"     6. Trademarks. This License does not grant permission to use the trade                 \n"
"        names, trademarks, service marks, or product names of the Licensor                  \n"
"        and its affiliates, except as required to comply with Section 4(c) of               \n"
"        the License and to reproduce the content of the NOTICE file.                        \n"
"                                                                                            \n"
"     You may obtain a copy of the Apache License at                                         \n"
"                                                                                            \n"
"         http://www.apache.org/licenses/LICENSE-2.0                                         \n"
"                                                                                            \n"
"     Unless required by applicable law or agreed to in writing, software                    \n"
"     distributed under the Apache License with the above modification is                    \n"
"     distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY   \n"
"     KIND, either express or implied. See the Apache License for the specific               \n"
"     language governing permissions and limitations under the Apache License.               \n"
"  ", None, QtGui.QApplication.UnicodeUTF8))

