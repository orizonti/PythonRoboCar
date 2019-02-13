# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DCMotorsUI.ui',
# licensing of 'DCMotorsUI.ui' applies.
#
# Created: Mon Jan  7 20:49:20 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DCMotors(object):
    def setupUi(self, DCMotors):
        DCMotors.setObjectName("DCMotors")
        DCMotors.resize(177, 197)
        DCMotors.setStyleSheet("QWidget\n"
"{\n"
"background-color: rgb(106, 106, 79);\n"
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
"}\n"
"\n"
"QLabel\n"
"{\n"
"background-color: rgb(170, 170, 127);\n"
"border: 2px solid line black;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"background-color: rgb(190, 190, 190);\n"
"border: 2px solid line black;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(DCMotors)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.lineBLeftMotor = QtWidgets.QLineEdit(DCMotors)
        self.lineBLeftMotor.setObjectName("lineBLeftMotor")
        self.gridLayout.addWidget(self.lineBLeftMotor, 2, 1, 1, 1)
        self.lineFLeftMotor = QtWidgets.QLineEdit(DCMotors)
        self.lineFLeftMotor.setObjectName("lineFLeftMotor")
        self.gridLayout.addWidget(self.lineFLeftMotor, 1, 1, 1, 1)
        self.butSetSpeedMotors = QtWidgets.QPushButton(DCMotors)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.butSetSpeedMotors.setFont(font)
        self.butSetSpeedMotors.setObjectName("butSetSpeedMotors")
        self.gridLayout.addWidget(self.butSetSpeedMotors, 5, 0, 1, 3)
        self.lineFRightMotor = QtWidgets.QLineEdit(DCMotors)
        self.lineFRightMotor.setObjectName("lineFRightMotor")
        self.gridLayout.addWidget(self.lineFRightMotor, 1, 2, 1, 1)
        self.lineBRightMotor = QtWidgets.QLineEdit(DCMotors)
        self.lineBRightMotor.setObjectName("lineBRightMotor")
        self.gridLayout.addWidget(self.lineBRightMotor, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(DCMotors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"border: 0px;\n"
"background-color: rgb(255, 255, 255,0);\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 3)
        self.butSetHandleControl = QtWidgets.QPushButton(DCMotors)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.butSetHandleControl.setFont(font)
        self.butSetHandleControl.setObjectName("butSetHandleControl")
        self.gridLayout.addWidget(self.butSetHandleControl, 6, 0, 1, 3)

        self.retranslateUi(DCMotors)
        QtCore.QMetaObject.connectSlotsByName(DCMotors)

    def retranslateUi(self, DCMotors):
        DCMotors.setWindowTitle(QtWidgets.QApplication.translate("DCMotors", "Form", None, -1))
        self.butSetSpeedMotors.setText(QtWidgets.QApplication.translate("DCMotors", "Установить", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("DCMotors", "Скорость двигателей", None, -1))
        self.butSetHandleControl.setText(QtWidgets.QApplication.translate("DCMotors", "Ручное управление", None, -1))

