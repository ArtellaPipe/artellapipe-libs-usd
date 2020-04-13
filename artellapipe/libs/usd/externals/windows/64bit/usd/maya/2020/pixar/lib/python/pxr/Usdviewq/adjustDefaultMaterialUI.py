# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'S:/jenkins/workspace/ecg-usd-full-windows/ecg-usd-build/usd/pxr/usdImaging/usdviewq/adjustDefaultMaterialUI.ui'
#
# Created: Sat Feb  1 10:28:15 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AdjustDefaultMaterial(object):
    def setupUi(self, AdjustDefaultMaterial):
        AdjustDefaultMaterial.setObjectName("AdjustDefaultMaterial")
        AdjustDefaultMaterial.resize(238, 123)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AdjustDefaultMaterial.sizePolicy().hasHeightForWidth())
        AdjustDefaultMaterial.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(AdjustDefaultMaterial)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ambientInt = QtGui.QLabel(AdjustDefaultMaterial)
        self.ambientInt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ambientInt.setObjectName("ambientInt")
        self.horizontalLayout.addWidget(self.ambientInt)
        self.ambientIntSpinBox = QtGui.QDoubleSpinBox(AdjustDefaultMaterial)
        self.ambientIntSpinBox.setDecimals(1)
        self.ambientIntSpinBox.setMaximum(1.0)
        self.ambientIntSpinBox.setSingleStep(0.1)
        self.ambientIntSpinBox.setObjectName("ambientIntSpinBox")
        self.horizontalLayout.addWidget(self.ambientIntSpinBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.specularInt = QtGui.QLabel(AdjustDefaultMaterial)
        self.specularInt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.specularInt.setObjectName("specularInt")
        self.horizontalLayout_2.addWidget(self.specularInt)
        self.specularIntSpinBox = QtGui.QDoubleSpinBox(AdjustDefaultMaterial)
        self.specularIntSpinBox.setDecimals(1)
        self.specularIntSpinBox.setMaximum(1.0)
        self.specularIntSpinBox.setSingleStep(0.1)
        self.specularIntSpinBox.setObjectName("specularIntSpinBox")
        self.horizontalLayout_2.addWidget(self.specularIntSpinBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.resetButton = QtGui.QPushButton(AdjustDefaultMaterial)
        self.resetButton.setAutoDefault(False)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_3.addWidget(self.resetButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.doneButton = QtGui.QPushButton(AdjustDefaultMaterial)
        self.doneButton.setObjectName("doneButton")
        self.horizontalLayout_3.addWidget(self.doneButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(AdjustDefaultMaterial)
        QtCore.QMetaObject.connectSlotsByName(AdjustDefaultMaterial)

    def retranslateUi(self, AdjustDefaultMaterial):
        AdjustDefaultMaterial.setProperty("comment", QtGui.QApplication.translate("AdjustDefaultMaterial", "\n"
"     Copyright 2017 Pixar                                                                   \n"
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
        AdjustDefaultMaterial.setWindowTitle(QtGui.QApplication.translate("AdjustDefaultMaterial", "Adjust Default Material", None, QtGui.QApplication.UnicodeUTF8))
        self.ambientInt.setText(QtGui.QApplication.translate("AdjustDefaultMaterial", "Ambient Intensity", None, QtGui.QApplication.UnicodeUTF8))
        self.specularInt.setText(QtGui.QApplication.translate("AdjustDefaultMaterial", "Specular Intensity", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("AdjustDefaultMaterial", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.doneButton.setText(QtGui.QApplication.translate("AdjustDefaultMaterial", "Done", None, QtGui.QApplication.UnicodeUTF8))

