# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQtGui.ui',
# licensing of 'PyQtGui.ui' applies.
#
# Created: Sat Jan  5 01:53:38 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(765, 886)
        Form.setStyleSheet("QWidget\n"
"{\n"
"background-color: rgb(93, 91, 95);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(170, 170, 127);\n"
"}")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listOutput_From_Micro = QtWidgets.QListWidget(Form)
        self.listOutput_From_Micro.setStyleSheet("QListWidget\n"
"{\n"
"border: 2px solid line black;\n"
"    background-color: rgb(170, 169, 151);\n"
"}")
        self.listOutput_From_Micro.setObjectName("listOutput_From_Micro")
        self.gridLayout_3.addWidget(self.listOutput_From_Micro, 2, 1, 1, 1)
        self.listOutput_To_Micro = QtWidgets.QListWidget(Form)
        self.listOutput_To_Micro.setStyleSheet("QListWidget\n"
"{\n"
"border: 2px solid line black;\n"
"    \n"
"    background-color: rgb(170, 169, 151);\n"
"}")
        self.listOutput_To_Micro.setObjectName("listOutput_To_Micro")
        self.gridLayout_3.addWidget(self.listOutput_To_Micro, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox\n"
"{\n"
"border: 2px solid line black;\n"
"    background-color: rgb(122, 135, 114);\n"
"}")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(-1, 18, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.ButStepMotorLeft = QtWidgets.QPushButton(self.groupBox)
        self.ButStepMotorLeft.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ArrowRight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButStepMotorLeft.setIcon(icon)
        self.ButStepMotorLeft.setIconSize(QtCore.QSize(80, 20))
        self.ButStepMotorLeft.setObjectName("ButStepMotorLeft")
        self.gridLayout.addWidget(self.ButStepMotorLeft, 0, 0, 1, 1)
        self.ButStepMotorRight = QtWidgets.QPushButton(self.groupBox)
        self.ButStepMotorRight.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ArrowLeft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButStepMotorRight.setIcon(icon1)
        self.ButStepMotorRight.setIconSize(QtCore.QSize(80, 20))
        self.ButStepMotorRight.setObjectName("ButStepMotorRight")
        self.gridLayout.addWidget(self.ButStepMotorRight, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox\n"
"{\n"
"border: 2px solid line black;\n"
"    background-color: rgb(190, 126, 94);\n"
"}\n"
"\n"
"")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ButtonClosePort = QtWidgets.QPushButton(self.groupBox_2)
        self.ButtonClosePort.setCheckable(True)
        self.ButtonClosePort.setChecked(False)
        self.ButtonClosePort.setObjectName("ButtonClosePort")
        self.gridLayout_2.addWidget(self.ButtonClosePort, 2, 0, 1, 1)
        self.ButtonSendData = QtWidgets.QPushButton(self.groupBox_2)
        self.ButtonSendData.setObjectName("ButtonSendData")
        self.gridLayout_2.addWidget(self.ButtonSendData, 0, 0, 1, 1)
        self.ButtonOpenPort = QtWidgets.QPushButton(self.groupBox_2)
        self.ButtonOpenPort.setObjectName("ButtonOpenPort")
        self.gridLayout_2.addWidget(self.ButtonOpenPort, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(225, 226, 195);\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(225, 226, 195);\n"
"}\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Form", "Шаговый двигатель", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Form", "COM PORT", None, -1))
        self.ButtonClosePort.setText(QtWidgets.QApplication.translate("Form", "ClosePort", None, -1))
        self.ButtonSendData.setText(QtWidgets.QApplication.translate("Form", "TEST CONNECT", None, -1))
        self.ButtonOpenPort.setText(QtWidgets.QApplication.translate("Form", "OpenPort", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "К микроконтроллеру", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "От микроконтроллера", None, -1))

