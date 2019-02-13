from PySide2.QtWidgets import QApplication, QWidget
from PySide2 import QtCore
from PySide2.QtCore import QByteArray,QDataStream,QThread
from TransferDataObjects import DC_Motor_Control_Data
from DCMotorsUI import *
from NetworkModule import NetworkConnectionClass

class DCMotorWindow(QWidget):
    def __init__(self,parent=None):
        super(DCMotorWindow,self).__init__(parent=parent)
        self.ui = Ui_DCMotors()
        self.ui.setupUi(self)

    def DisplayState(self,MotorState:DC_Motor_Control_Data):
        self.ui.lineBLeftMotor.setText(str(MotorState.Speed1))
        self.ui.lineBRightMotor.setText(str(MotorState.Speed2))

        self.ui.lineFLeftMotor.setText(str(MotorState.Speed3))
        self.ui.lineFRightMotor.setText(str(MotorState.Speed4))



class DCCMotorControlClass(QtCore.QObject):
    def __init__(self, parent=None,MainController=None):
        super(DCCMotorControlClass,self).__init__(parent=parent)
        self.Controller = MainController
        self.MotorsState = DC_Motor_Control_Data()
        self.Display = DCMotorWindow()


    def MoveDCMotors(self,MotorsSpeed:DC_Motor_Control_Data):
        self.STEP_MOTOR_COMMAND = QByteArray()
        stream = QDataStream(self.STEP_MOTOR_COMMAND,QtCore.QIODevice.ReadWrite)

        stream.writeInt8(self.MotorsState.HEADER_B1)
        stream.writeInt8(self.MotorsState.HEADER_B2)
        stream.writeInt8(self.MotorsState.UNIT_SIZE)

        stream.writeInt16(self.MotorsState.Speed1)
        stream.writeInt16(self.MotorsState.Speed2)
        stream.writeInt16(self.MotorsState.Speed3)
        stream.writeInt16(self.MotorsState.Speed4)

    def __lshift__(self, Sender:NetworkConnectionClass):
        Sender >> self.MotorsState
        self.Display.DisplayState(self.MotorsState)

        return 0
