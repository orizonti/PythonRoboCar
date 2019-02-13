from PyQt5 import QtSerialPort
from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import QObject


class ComPortClass(QObject):
    def __init__(self):

        self.SerialPort = QtSerialPort.QSerialPort()
        self.SerialPort.setBaudRate(115200)
        self.SerialPort.setPortName("COM8")
        self.SerialPort.readyRead.connect(self.ReadData)

        self.DATA_WAIT_SIZE = 0
        self.DATA_BUFFER = QByteArray()
        self.DATA_MESSAGE = QByteArray()
        self.FLAG_WAIT_DATA = False
    def OpenPort(self):
        result = self.SerialPort.open(QtSerialPort.QSerialPort.ReadWrite)
        print(" PORT - ",self.SerialPort.portName()," OPENED")


        #self.Window.ui.ButtonOpenPort.clicked.connect(self.OpenPort)
        #self.Window.ui.ButtonSendData.clicked.connect(self.TestCOMConnection)
        #self.Window.ui.ButStepMotorRight.clicked.connect(lambda: self.MotorControl.MoveStepMotor(NumberMotor=0,Direction=1))
        #self.Window.ui.ButStepMotorLeft.clicked.connect(lambda: self.MotorControl.MoveStepMotor(NumberMotor=1,Direction=-1))


    def TestCOMConnection(self):
        self.HEADER_DATA = bytearray.fromhex("A1 F1 00")
        COMMAND_HEADER = bytearray.fromhex("01")
        self.DATA = COMMAND_HEADER + bytearray("TEST MESSAGE","utf-8")
        self.HEADER_DATA[2] = len(self.DATA)
        result = self.SerialPort.write(self.HEADER_DATA)
        result = self.SerialPort.write(self.DATA)
        print("SEND MESSAGE - ",self.DATA)

    def ClosePort(self):
        result = self.SerialPort.close()

    def ReadData(self):
        New_Data = self.SerialPort.readAll()
        self.DATA_BUFFER.append(New_Data)
        #print("BUFFER -  " ,self.DATA_BUFFER.toHex(),"SIZE - ",self.DATA_BUFFER.length(),"WAIT - ",self.DATA_WAIT_SIZE)

        while(self.DATA_BUFFER.length() >= 3):

            if(self.DATA_BUFFER[0] == b'\xF1' and self.DATA_BUFFER[1] == b'\xA1'):
                self.DATA_WAIT_SIZE = self.DATA_BUFFER[2][0]
                self.DATA_BUFFER.remove(0,3)

            if(self.DATA_BUFFER.length() >= self.DATA_WAIT_SIZE):
                self.DATA_MESSAGE.clear()
                self.DATA_MESSAGE.append(self.DATA_BUFFER)
                self.DATA_BUFFER.remove(0,self.DATA_WAIT_SIZE)
                self.DATA_MESSAGE.truncate(self.DATA_WAIT_SIZE)
                print(self.DATA_BUFFER.toHex())
                self.Window.AddText("    " + self.DATA_MESSAGE.data().decode(encoding="utf-8"),0)
            else:
                break;
