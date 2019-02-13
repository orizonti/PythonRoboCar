# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowContainer.ui',
# licensing of 'MainWindowContainer.ui' applies.
#
# Created: Mon Jan  7 20:49:17 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindowContainer(object):
    def setupUi(self, MainWindowContainer):
        MainWindowContainer.setObjectName("MainWindowContainer")
        MainWindowContainer.resize(990, 788)
        MainWindowContainer.setStyleSheet("QWidget\n"
"{\n"
"background-color: rgb(74, 74, 74);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(MainWindowContainer)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(MainWindowContainer)
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setStyleSheet("QGraphicsView\n"
"{\n"
"    background-image: url(D:\\grid-png-43571.png);\n"
"    background-repeat: repeat-xy;\n"
"border:2px solid line black;\n"
"    background-color: rgb(129, 129, 113);\n"
"}")
        self.graphicsView.setInteractive(True)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.retranslateUi(MainWindowContainer)
        QtCore.QMetaObject.connectSlotsByName(MainWindowContainer)

    def retranslateUi(self, MainWindowContainer):
        MainWindowContainer.setWindowTitle(QtWidgets.QApplication.translate("MainWindowContainer", "Form", None, -1))

