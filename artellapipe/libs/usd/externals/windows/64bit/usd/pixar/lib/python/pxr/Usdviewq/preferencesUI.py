# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/dev/artellapipe/artellapipe-libs-usd/usd/USD/pxr/usdImaging/usdviewq/preferencesUI.ui'
#
# Created: Sat Aug 22 05:13:16 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(295, 99)
        self.verticalLayout = QtGui.QVBoxLayout(Preferences)
        self.verticalLayout.setObjectName("verticalLayout")
        self.prefsOverButtonsLayout = QtGui.QVBoxLayout()
        self.prefsOverButtonsLayout.setObjectName("prefsOverButtonsLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fontSizeLabel = QtGui.QLabel(Preferences)
        self.fontSizeLabel.setObjectName("fontSizeLabel")
        self.horizontalLayout_3.addWidget(self.fontSizeLabel)
        self.fontSizeSpinBox = QtGui.QSpinBox(Preferences)
        self.fontSizeSpinBox.setMinimum(6)
        self.fontSizeSpinBox.setProperty("value", 10)
        self.fontSizeSpinBox.setObjectName("fontSizeSpinBox")
        self.horizontalLayout_3.addWidget(self.fontSizeSpinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.prefsOverButtonsLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.prefsOverButtonsLayout.addItem(spacerItem1)
        self.line = QtGui.QFrame(Preferences)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.prefsOverButtonsLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.buttonBox = QtGui.QDialogButtonBox(Preferences)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.prefsOverButtonsLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.prefsOverButtonsLayout)

        self.retranslateUi(Preferences)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QtGui.QApplication.translate("Preferences", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        Preferences.setProperty("comment", QtGui.QApplication.translate("Preferences", "\n"
"     Copyright 2020 Pixar                                                                   \n"
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
        self.fontSizeLabel.setText(QtGui.QApplication.translate("Preferences", "Font Size", None, QtGui.QApplication.UnicodeUTF8))

