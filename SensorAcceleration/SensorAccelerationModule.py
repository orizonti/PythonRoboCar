from PySide2.QtWidgets import QApplication, QWidget
from PySide2 import QtCore
from PySide2.QtCore import QByteArray,QDataStream,QThread,QObject

from SensorAccelerationUI import Ui_SensorAcceleration
from TransferDataObjects import Accelerometer_Data
from NetworkModule import NetworkConnectionClass

class AccelerationWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_SensorAcceleration()
        self.ui.setupUi(self)

    def DisplayState(self,SensorState:Accelerometer_Data):
        self.ui.labelAccelX.setText(str(SensorState.AccelX))
        self.ui.labelAccelY.setText(str(SensorState.AccelY))
        self.ui.labelAccelZ.setText(str(SensorState.AccelZ))

        self.ui.labelAngleSpeedX.setText(str(SensorState.AngularSpeedX))
        self.ui.labelAngleSpeedY.setText(str(SensorState.AngularSpeedY))
        self.ui.labelAngleSpeedZ.setText(str(SensorState.AngularSpeedZ))

        self.ui.labelAzimuth.setText(str(SensorState.Azimuth))
        self.ui.labelElevation.setText(str(SensorState.Elevation))
        self.ui.labelPitch.setText(str(SensorState.Pitch))


class SensorAccelerationClass(QObject):
    def __init__(self,parent=None):
        super(SensorAccelerationClass,self).__init__(parent=parent)
        self.Display = AccelerationWindow()
        self.SensorState = Accelerometer_Data()

    def __lshift__(self, Sender:NetworkConnectionClass):
          Sender >> self.SensorState
          self.Display.DisplayState(self.SensorState)


