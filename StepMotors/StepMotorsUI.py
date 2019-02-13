# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StepMotorsUI.ui',
# licensing of 'StepMotorsUI.ui' applies.
#
# Created: Mon Jan  7 20:49:07 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_StepMotors(object):
    def setupUi(self, StepMotors):
        StepMotors.setObjectName("StepMotors")
        StepMotors.resize(324, 384)
        StepMotors.setStyleSheet("QWidget\n"
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
"QSlider\n"
"{\n"
"background-color: rgb(170, 170, 127);\n"
"border: 2px solid line black;\n"
"}")
        self.gridLayout_3 = QtWidgets.QGridLayout(StepMotors)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridGroupBox = QtWidgets.QGroupBox(StepMotors)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.gridGroupBox.setFont(font)
        self.gridGroupBox.setStyleSheet("QGroupBox\n"
"{\n"
"background-color: rgb(120, 161, 66);\n"
"border: 2px solid line black;\n"
"}")
        self.gridGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.labelStepMotorAngle1 = QtWidgets.QLabel(self.gridGroupBox)
        self.labelStepMotorAngle1.setMinimumSize(QtCore.QSize(40, 0))
        self.labelStepMotorAngle1.setObjectName("labelStepMotorAngle1")
        self.gridLayout.addWidget(self.labelStepMotorAngle1, 0, 1, 1, 1)
        self.labelStepMotorAngle2 = QtWidgets.QLabel(self.gridGroupBox)
        self.labelStepMotorAngle2.setMinimumSize(QtCore.QSize(40, 0))
        self.labelStepMotorAngle2.setObjectName("labelStepMotorAngle2")
        self.gridLayout.addWidget(self.labelStepMotorAngle2, 1, 1, 1, 1)
        self.labelStepMotorAngle3 = QtWidgets.QLabel(self.gridGroupBox)
        self.labelStepMotorAngle3.setMinimumSize(QtCore.QSize(40, 0))
        self.labelStepMotorAngle3.setObjectName("labelStepMotorAngle3")
        self.gridLayout.addWidget(self.labelStepMotorAngle3, 2, 1, 1, 1)
        self.sliderStepMotorAngle1 = QtWidgets.QSlider(self.gridGroupBox)
        self.sliderStepMotorAngle1.setOrientation(QtCore.Qt.Horizontal)
        self.sliderStepMotorAngle1.setObjectName("sliderStepMotorAngle1")
        self.gridLayout.addWidget(self.sliderStepMotorAngle1, 0, 2, 1, 1)
        self.sliderStepMotorAngle2 = QtWidgets.QSlider(self.gridGroupBox)
        self.sliderStepMotorAngle2.setOrientation(QtCore.Qt.Horizontal)
        self.sliderStepMotorAngle2.setObjectName("sliderStepMotorAngle2")
        self.gridLayout.addWidget(self.sliderStepMotorAngle2, 1, 2, 1, 1)
        self.sliderStepMotorAngle3 = QtWidgets.QSlider(self.gridGroupBox)
        self.sliderStepMotorAngle3.setOrientation(QtCore.Qt.Horizontal)
        self.sliderStepMotorAngle3.setObjectName("sliderStepMotorAngle3")
        self.gridLayout.addWidget(self.sliderStepMotorAngle3, 2, 2, 1, 1)
        self.gridLayout_3.addWidget(self.gridGroupBox, 0, 0, 1, 1)
        self.gridGroupBox_2 = QtWidgets.QGroupBox(StepMotors)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.gridGroupBox_2.setFont(font)
        self.gridGroupBox_2.setStyleSheet("QGroupBox\n"
"{\n"
"background-color: rgb(170, 144, 93);\n"
"border: 2px solid line black;\n"
"}")
        self.gridGroupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gridGroupBox_2.setObjectName("gridGroupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridGroupBox_2)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridGroupBox_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridGroupBox_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridGroupBox_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.labelStepMotorSpeed1 = QtWidgets.QLabel(self.gridGroupBox_2)
        self.labelStepMotorSpeed1.setMinimumSize(QtCore.QSize(40, 0))
        self.labelStepMotorSpeed1.setObjectName("labelStepMotorSpeed1")
        self.gridLayout_2.addWidget(self.labelStepMotorSpeed1, 0, 1, 1, 1)
        self.labelStepMotorSpeed2 = QtWidgets.QLabel(self.gridGroupBox_2)
        self.labelStepMotorSpeed2.setMinimumSize(QtCore.QSize(40, 0))
        self.labelStepMotorSpeed2.setObjectName("labelStepMotorSpeed2")
        self.gridLayout_2.addWidget(self.labelStepMotorSpeed2, 1, 1, 1, 1)
        self.labelStepMotorSpeed3 = QtWidgets.QLabel(self.gridGroupBox_2)
        self.labelStepMotorSpeed3.setMinimumSize(QtCore.QSize(40, 0))
        self.labelStepMotorSpeed3.setObjectName("labelStepMotorSpeed3")
        self.gridLayout_2.addWidget(self.labelStepMotorSpeed3, 2, 1, 1, 1)
        self.sliderStepMotorAngle1_2 = QtWidgets.QSlider(self.gridGroupBox_2)
        self.sliderStepMotorAngle1_2.setOrientation(QtCore.Qt.Horizontal)
        self.sliderStepMotorAngle1_2.setObjectName("sliderStepMotorAngle1_2")
        self.gridLayout_2.addWidget(self.sliderStepMotorAngle1_2, 0, 2, 1, 1)
        self.sliderStepMotorAngle2_2 = QtWidgets.QSlider(self.gridGroupBox_2)
        self.sliderStepMotorAngle2_2.setOrientation(QtCore.Qt.Horizontal)
        self.sliderStepMotorAngle2_2.setObjectName("sliderStepMotorAngle2_2")
        self.gridLayout_2.addWidget(self.sliderStepMotorAngle2_2, 1, 2, 1, 1)
        self.sliderStepMotorAngle3_2 = QtWidgets.QSlider(self.gridGroupBox_2)
        self.sliderStepMotorAngle3_2.setStyleSheet("")
        self.sliderStepMotorAngle3_2.setOrientation(QtCore.Qt.Horizontal)
        self.sliderStepMotorAngle3_2.setObjectName("sliderStepMotorAngle3_2")
        self.gridLayout_2.addWidget(self.sliderStepMotorAngle3_2, 2, 2, 1, 1)
        self.gridLayout_3.addWidget(self.gridGroupBox_2, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(StepMotors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox\n"
"{\n"
"background-color: rgb(149, 133, 51);\n"
"border: 2px solid line black;\n"
"}")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.butMotorCamManualOn = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.butMotorCamManualOn.setFont(font)
        self.butMotorCamManualOn.setObjectName("butMotorCamManualOn")
        self.horizontalLayout.addWidget(self.butMotorCamManualOn)
        self.butMotorSensor1ManualOn = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.butMotorSensor1ManualOn.setFont(font)
        self.butMotorSensor1ManualOn.setObjectName("butMotorSensor1ManualOn")
        self.horizontalLayout.addWidget(self.butMotorSensor1ManualOn)
        self.butMotorSensor2ManualOn = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.butMotorSensor2ManualOn.setFont(font)
        self.butMotorSensor2ManualOn.setObjectName("butMotorSensor2ManualOn")
        self.horizontalLayout.addWidget(self.butMotorSensor2ManualOn)
        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)

        self.retranslateUi(StepMotors)
        QtCore.QMetaObject.connectSlotsByName(StepMotors)

    def retranslateUi(self, StepMotors):
        StepMotors.setWindowTitle(QtWidgets.QApplication.translate("StepMotors", "Form", None, -1))
        self.gridGroupBox.setTitle(QtWidgets.QApplication.translate("StepMotors", "Шаговые двигатели угол", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("StepMotors", "Дальномер п", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("StepMotors", "Дальномер л", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("StepMotors", "Камера ", None, -1))
        self.labelStepMotorAngle1.setText(QtWidgets.QApplication.translate("StepMotors", "0", None, -1))
        self.labelStepMotorAngle2.setText(QtWidgets.QApplication.translate("StepMotors", "0", None, -1))
        self.labelStepMotorAngle3.setText(QtWidgets.QApplication.translate("StepMotors", "0", None, -1))
        self.gridGroupBox_2.setTitle(QtWidgets.QApplication.translate("StepMotors", "Шаговые двигатели скорость", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("StepMotors", "Дальномер п", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("StepMotors", "Дальномер л", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("StepMotors", "Камера ", None, -1))
        self.labelStepMotorSpeed1.setText(QtWidgets.QApplication.translate("StepMotors", "0", None, -1))
        self.labelStepMotorSpeed2.setText(QtWidgets.QApplication.translate("StepMotors", "0", None, -1))
        self.labelStepMotorSpeed3.setText(QtWidgets.QApplication.translate("StepMotors", "0", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("StepMotors", "Ручное управление", None, -1))
        self.butMotorCamManualOn.setText(QtWidgets.QApplication.translate("StepMotors", "Камера", None, -1))
        self.butMotorSensor1ManualOn.setText(QtWidgets.QApplication.translate("StepMotors", "Дальномер л", None, -1))
        self.butMotorSensor2ManualOn.setText(QtWidgets.QApplication.translate("StepMotors", "Дальномер п", None, -1))

