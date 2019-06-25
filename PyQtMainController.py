import sys
sys.path.append("./MainWindowModule")
sys.path.append("./NetworkConnection")
sys.path.append("./SensorAcceleration")
sys.path.append("./COMPort")
sys.path.append("./DCMotors")
sys.path.append("./StepMotors")
sys.path.append("./PlotGraphics")

from MainWindowModule import MainWindowClass
from NetworkModule import NetworkConnectionClass
from SensorAccelerationModule import SensorAccelerationClass
from DCMotorModule import DCCMotorControlClass
from StepMotorModule import StepMotorControlClass

from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QWidget,QGroupBox,QHBoxLayout
from PySide2.QtCore import QByteArray,QDataStream,QThread,QTimer,QObject, Signal, Slot
from TransferDataObjects import *
from PlotGraphicsModule import ApplicationWindow
from PlotGraphicsModule import LineGraphicsPlot,GroupWindowModule
from PySide2.QtCharts import QtCharts


class MainController(QtCore.QObject):
    SignalSendData = Signal(str)
    def __init__(self):
        super(MainController,self).__init__()
        self.MainWindow = MainWindowClass()
        self.Network = NetworkConnectionClass()
        self.StepMotors = StepMotorControlClass()
        self.DCMotors = DCCMotorControlClass()
        self.SensorAccel = SensorAccelerationClass()

        self.MainTimer = QTimer
        self.Network.SignalFrameDataAvailable.connect(self.PerformNetworkData)

        self.SignalSendData.connect(self.Network.SendData)

        self.ChartPlot1 = LineGraphicsPlot()
        self.ChartPlot2 = LineGraphicsPlot()
        self.ChartPlot3 = LineGraphicsPlot()
        self.ChartPlot4 = LineGraphicsPlot()


        self.ChartView1 = QtCharts.QChartView(self.ChartPlot1)
        self.ChartView2 = QtCharts.QChartView(self.ChartPlot2)
        self.ChartView3 = QtCharts.QChartView(self.ChartPlot3)
        self.ChartView4 = QtCharts.QChartView(self.ChartPlot4)

        self.Group = GroupWindowModule()
        self.Group.addWidget(self.ChartView1)
        self.Group.addWidget(self.ChartView2)
        self.Group.addWidget(self.ChartView3)
        self.Group.addWidget(self.ChartView4)

        self.MainWindow.SetModuleWidget(-400,590,self.Group)
        self.Group.show()


        self.MainWindow.SetModuleWidget(-400,90,self.Network.Display)
        self.MainWindow.SetModuleWidget(100,90,self.SensorAccel.Display)

        self.MainWindow.SetModuleWidget(390,90,self.DCMotors.Display)
        self.MainWindow.SetModuleWidget(600,90,self.StepMotors.Display)


        self.MainWindow.move(10,10)
        self.MainWindow.show()
        self.MainWindow.resize(1900,900)

        self.ThreadNetwork = QThread()
        self.Network.moveToThread(self.ThreadNetwork)
        self.ThreadNetwork.start()

    def PerformNetworkData(self): #Recieve SignalFrameAvailable from NetworkModule
        HEADER = DataTransferHeader()
        while self.Network.bytesAvailable >= self.Network.MinTransferUnit:
            self.Network >> HEADER
            print("         HEADER - ",hex(HEADER.HEADER_B1),hex(HEADER.HEADER_B2))

            if HEADER.HEADER_B1 == 0xF1:
                if HEADER.HEADER_B2 == 0xD1:
                    self.DCMotors << self.Network
                if HEADER.HEADER_B2 == 0xD2:
                    self.StepMotors << self.Network
                if HEADER.HEADER_B2 == 0xD3:
                    self.SensorAccel << self.Network
                if HEADER.HEADER_B2 == 0xC1:
                    Data = ConnectCheckRequest()
                    self.Network >> Data
                    self.Network.SignalDataRec.emit("CHECK CONNECT - " + str(Data.Connect),0)
                    #DISPLAY STRING IN NetworkModuleUI
                else:
                    pass



if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainBlock = MainController()


    sys.exit(app.exec_())

