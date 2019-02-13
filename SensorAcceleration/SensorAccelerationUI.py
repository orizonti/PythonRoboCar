# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SensorAccelerationUI.ui',
# licensing of 'SensorAccelerationUI.ui' applies.
#
# Created: Mon Jan  7 20:49:10 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SensorAcceleration(object):
    def setupUi(self, SensorAcceleration):
        SensorAcceleration.setObjectName("SensorAcceleration")
        SensorAcceleration.resize(239, 398)
        SensorAcceleration.setStyleSheet("QWidget\n"
"{\n"
"background-color: rgb(102, 102, 102);\n"
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
        self.gridLayout_4 = QtWidgets.QGridLayout(SensorAcceleration)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(SensorAcceleration)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox\n"
"{\n"
"background-color: rgb(118, 166, 123);\n"
"border: 2px solid line black;\n"
"}")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(-1, 16, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.labelAccelX = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelAccelX.setFont(font)
        self.labelAccelX.setObjectName("labelAccelX")
        self.gridLayout.addWidget(self.labelAccelX, 1, 2, 1, 1)
        self.labelAccelY = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelAccelY.setFont(font)
        self.labelAccelY.setObjectName("labelAccelY")
        self.gridLayout.addWidget(self.labelAccelY, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.labelAccelZ = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelAccelZ.setFont(font)
        self.labelAccelZ.setObjectName("labelAccelZ")
        self.gridLayout.addWidget(self.labelAccelZ, 4, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(SensorAcceleration)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox\n"
"{\n"
"background-color: rgb(161, 102, 50);\n"
"border: 2px solid line black;\n"
"}")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(-1, 16, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.labelAngleSpeedX = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelAngleSpeedX.setFont(font)
        self.labelAngleSpeedX.setObjectName("labelAngleSpeedX")
        self.gridLayout_2.addWidget(self.labelAngleSpeedX, 1, 2, 1, 1)
        self.labelAngleSpeedY = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelAngleSpeedY.setFont(font)
        self.labelAngleSpeedY.setObjectName("labelAngleSpeedY")
        self.gridLayout_2.addWidget(self.labelAngleSpeedY, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 1, 1, 1)
        self.labelAngleSpeedZ = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelAngleSpeedZ.setFont(font)
        self.labelAngleSpeedZ.setObjectName("labelAngleSpeedZ")
        self.gridLayout_2.addWidget(self.labelAngleSpeedZ, 4, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(SensorAcceleration)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QGroupBox\n"
"{\n"
"background-color: rgb(76, 122, 131);\n"
"border: 2px solid line black;\n"
"}")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setContentsMargins(-1, 16, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 1, 1, 1)
        self.labelAzimuth = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelAzimuth.setFont(font)
        self.labelAzimuth.setObjectName("labelAzimuth")
        self.gridLayout_3.addWidget(self.labelAzimuth, 1, 2, 1, 1)
        self.labelElevation = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelElevation.setFont(font)
        self.labelElevation.setObjectName("labelElevation")
        self.gridLayout_3.addWidget(self.labelElevation, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 1, 1, 1)
        self.labelPitch = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelPitch.setFont(font)
        self.labelPitch.setObjectName("labelPitch")
        self.gridLayout_3.addWidget(self.labelPitch, 4, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.retranslateUi(SensorAcceleration)
        QtCore.QMetaObject.connectSlotsByName(SensorAcceleration)

    def retranslateUi(self, SensorAcceleration):
        SensorAcceleration.setWindowTitle(QtWidgets.QApplication.translate("SensorAcceleration", "Form", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("SensorAcceleration", "Акселерометр", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("SensorAcceleration", "X", None, -1))
        self.labelAccelX.setText(QtWidgets.QApplication.translate("SensorAcceleration", "0", None, -1))
        self.labelAccelY.setText(QtWidgets.QApplication.translate("SensorAcceleration", "0", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("SensorAcceleration", "Y", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("SensorAcceleration", "Z", None, -1))
        self.labelAccelZ.setText(QtWidgets.QApplication.translate("SensorAcceleration", "0", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("SensorAcceleration", "Гироскоп", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("SensorAcceleration", "X", None, -1))
        self.labelAngleSpeedX.setText(QtWidgets.QApplication.translate("SensorAcceleration", "0", None, -1))
        self.labelAngleSpeedY.setText(QtWidgets.QApplication.translate("SensorAcceleration", "0", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("SensorAcceleration", "Y", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("SensorAcceleration", "Z", None, -1))
        self.labelAngleSpeedZ.setText(QtWidgets.QApplication.translate("SensorAcceleration", "0", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("SensorAcceleration", "Магнетометр", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("SensorAcceleration", "Азимут", None, -1))
        self.labelAzimuth.setText(QtWidgets.QApplication.translate("SensorAcceleration", "0", None, -1))
        self.labelElevation.setText(QtWidgets.QApplication.translate("SensorAcceleration", "0", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("SensorAcceleration", "Угол места", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("SensorAcceleration", "Наклон", None, -1))
        self.labelPitch.setText(QtWidgets.QApplication.translate("SensorAcceleration", "0", None, -1))

