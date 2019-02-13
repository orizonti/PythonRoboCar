from PySide2.QtWidgets import QApplication, QWidget
from PySide2 import QtCore
from PySide2.QtCore import QByteArray,QDataStream,QThread
from TransferDataObjects import Step_Motor_Control_Data
from StepMotorsUI import *
from NetworkModule import NetworkConnectionClass

class StepMotorWindow(QWidget):
    def __init__(self,parent=None):
        super(StepMotorWindow,self).__init__(parent=parent)
        self.ui = Ui_StepMotors()
        self.ui.setupUi(self)

    def DisplayState(self,MotorState:Step_Motor_Control_Data):
        self.ui.labelStepMotorAngle1.setText(str(MotorState.AngleMotor1))
        self.ui.labelStepMotorAngle2.setText(str(MotorState.AngleMotor2))
        self.ui.labelStepMotorAngle3.setText(str(MotorState.AngleMotor3))

        self.ui.labelStepMotorSpeed1.setText(str(MotorState.SpeedMotor1))
        self.ui.labelStepMotorSpeed2.setText(str(MotorState.SpeedMotor2))
        self.ui.labelStepMotorSpeed3.setText(str(MotorState.SpeedMotor3))


class StepMotorControlClass(QtCore.QObject):
    def __init__(self, parent=None,MainController=None):
        super(StepMotorControlClass,self).__init__(parent=parent)
        self.Controller = MainController
        self.StepMotorState = Step_Motor_Control_Data()
        self.Display = StepMotorWindow()

    def MoveStepMotor(self,MotorCommand:Step_Motor_Control_Data):

        stream = QDataStream(self.STEP_MOTOR_COMMAND,QtCore.QIODevice.ReadWrite)
        stream.writeInt8(MotorCommand.HEADER_B1)
        stream.writeInt8(MotorCommand.HEADER_B2)
        stream.writeInt8(MotorCommand.UNIT_SIZE)

        stream.writeInt16(MotorCommand.SpeedMotor1)
        stream.writeInt16(MotorCommand.SpeedMotor2)
        stream.writeInt16(MotorCommand.SpeedMotor3)

        stream.writeInt16(MotorCommand.AngleMotor1)
        stream.writeInt16(MotorCommand.AngleMotor2)
        stream.writeInt16(MotorCommand.AngleMotor3)

    def __lshift__(self, Sender:NetworkConnectionClass):
        Sender >> self.StepMotorState
        self.Display.DisplayState(self.StepMotorState)

        return 0
