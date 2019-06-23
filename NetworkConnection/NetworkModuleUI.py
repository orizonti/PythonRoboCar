# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NetworkModuleUI.ui',
# licensing of 'NetworkModuleUI.ui' applies.
#
# Created: Sun Jun 23 20:16:09 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_NetworkControl(object):
    def setupUi(self, NetworkControl):
        NetworkControl.setObjectName("NetworkControl")
        NetworkControl.resize(413, 465)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NetworkControl.sizePolicy().hasHeightForWidth())
        NetworkControl.setSizePolicy(sizePolicy)
        NetworkControl.setStyleSheet("QWidget\n"
"{\n"
"background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(130, 130, 130, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton#evilButton {\n"
"    background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"QPushButton#evilButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(NetworkControl)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidgetRecieveData = QtWidgets.QListWidget(NetworkControl)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.listWidgetRecieveData.setFont(font)
        self.listWidgetRecieveData.setStyleSheet("QListWidget\n"
"{\n"
"background-color: rgb(177, 177, 177);\n"
"border: 2px solid line black;\n"
"}\n"
"")
        self.listWidgetRecieveData.setObjectName("listWidgetRecieveData")
        self.gridLayout.addWidget(self.listWidgetRecieveData, 5, 0, 1, 2)
        self.listWidgetSendData = QtWidgets.QListWidget(NetworkControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetSendData.sizePolicy().hasHeightForWidth())
        self.listWidgetSendData.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.listWidgetSendData.setFont(font)
        self.listWidgetSendData.setStyleSheet("QListWidget\n"
"{\n"
"background-color: rgb(177, 177, 177);\n"
"border: 2px solid line black;\n"
"}\n"
"")
        self.listWidgetSendData.setObjectName("listWidgetSendData")
        self.gridLayout.addWidget(self.listWidgetSendData, 5, 2, 1, 2)
        self.labelSendData = QtWidgets.QLabel(NetworkControl)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelSendData.setFont(font)
        self.labelSendData.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgb(255, 255, 255,0);\n"
"    color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"")
        self.labelSendData.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSendData.setObjectName("labelSendData")
        self.gridLayout.addWidget(self.labelSendData, 3, 2, 1, 2)
        self.pushButton = QtWidgets.QPushButton(NetworkControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 2, 1, 2)
        self.labelImageSocket = QtWidgets.QLabel(NetworkControl)
        self.labelImageSocket.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgb(170, 170, 127);\n"
"border: 2px solid line black;\n"
"}")
        self.labelImageSocket.setText("")
        self.labelImageSocket.setObjectName("labelImageSocket")
        self.gridLayout.addWidget(self.labelImageSocket, 1, 0, 1, 2)
        self.labelDataSocket = QtWidgets.QLabel(NetworkControl)
        self.labelDataSocket.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgb(170, 170, 127);\n"
"border: 2px solid line black;\n"
"}")
        self.labelDataSocket.setText("")
        self.labelDataSocket.setObjectName("labelDataSocket")
        self.gridLayout.addWidget(self.labelDataSocket, 0, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(NetworkControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setStyleSheet("QCheckBox\n"
"{\n"
"background-color: rgb(198, 31, 19);\n"
"border: 2px solid line black;\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.label_5 = QtWidgets.QLabel(NetworkControl)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgb(255, 255, 255,0);\n"
"    \n"
"    color: rgb(222, 222, 166);\n"
"}\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_2 = QtWidgets.QCheckBox(NetworkControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setStyleSheet("QCheckBox\n"
"{\n"
"background-color: rgb(198, 31, 19);\n"
"border: 2px solid line black;\n"
"}")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.label_6 = QtWidgets.QLabel(NetworkControl)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgb(255, 255, 255,0);\n"
"    \n"
"    color: rgb(222, 222, 166);\n"
"}\n"
"")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 2, 1, 2)
        self.ButShowDataTransfer = QtWidgets.QPushButton(NetworkControl)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.ButShowDataTransfer.setFont(font)
        self.ButShowDataTransfer.setObjectName("ButShowDataTransfer")
        self.gridLayout.addWidget(self.ButShowDataTransfer, 6, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(NetworkControl)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgb(255, 255, 255,0);\n"
"    color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)

        self.retranslateUi(NetworkControl)
        QtCore.QMetaObject.connectSlotsByName(NetworkControl)

    def retranslateUi(self, NetworkControl):
        NetworkControl.setWindowTitle(QtWidgets.QApplication.translate("NetworkControl", "Form", None, -1))
        self.labelSendData.setText(QtWidgets.QApplication.translate("NetworkControl", "Передача", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("NetworkControl", "Тест", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("NetworkControl", "Работа     ", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("NetworkControl", "Сокет данных", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("NetworkControl", "Работа     ", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("NetworkControl", "Сотек камеры", None, -1))
        self.ButShowDataTransfer.setText(QtWidgets.QApplication.translate("NetworkControl", "Вывод", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("NetworkControl", "Прием", None, -1))

