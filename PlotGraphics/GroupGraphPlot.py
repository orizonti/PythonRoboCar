# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupGraphPlot.ui',
# licensing of 'GroupGraphPlot.ui' applies.
#
# Created: Sun Jan 13 22:59:39 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_GroupGraphWindow(object):
    def setupUi(self, GroupGraphWindow):
        GroupGraphWindow.setObjectName("GroupGraphWindow")
        GroupGraphWindow.resize(508, 417)
        GroupGraphWindow.setStyleSheet("QWidget\n"
"{\n"
"background-color: rgb(102, 101, 92);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(GroupGraphWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.retranslateUi(GroupGraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GroupGraphWindow)

    def retranslateUi(self, GroupGraphWindow):
        GroupGraphWindow.setWindowTitle(QtWidgets.QApplication.translate("GroupGraphWindow", "Form", None, -1))

