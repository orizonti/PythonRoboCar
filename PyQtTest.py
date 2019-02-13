#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore,QtGui,uic
from PyQtGui import Ui_Form
from PyQt5 import QtSerialPort
import PyQtMainController
import sys
 
class MainWindow(QWidget):
    #SignalFire = QtCore.pyqtSignal()
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def AddText(self,Text = "",Direction = 0):
        if(Direction == 0):
            self.ui.listOutput_From_Micro.addItem(Text)
        if(Direction == 1):
            self.ui.listOutput_To_Micro.addItem(Text)

    



if __name__ == '__main__':

    app = QApplication([])

    MainController = PyQtMainController.MainController()
    MainController.Window.show()


    sys.exit(app.exec_())

