from PySide2.QtCore import QDataStream
from PySide2.QtCore import QBuffer,QDataStream,QByteArray

class DataTransferHeader(object):
    def __init__(self,HB1=0x00,HB2=0x00,UNIT=6):
        self.HEADER_B1 = HB1
        self.HEADER_B2 = HB2
        self.UNIT_SIZE = UNIT
        self.MESSAGE_SIZE = 0

    def __lshift__(self, Sender:QDataStream):
        self.HEADER_B1 = Sender.readInt16()
        self.HEADER_B2 = Sender.readInt16()
        self.MESSAGE_SIZE = Sender.readInt16()

    def __rshift__(self, Sender:QDataStream):
        print("HEADER LOAD TO DATA STREAM")
        Sender.writeInt16(self.HEADER_B1)
        Sender.writeInt16(self.HEADER_B2)
        Sender.writeInt16(self.MESSAGE_SIZE)

class DC_Motor_Control_Data(DataTransferHeader):
    def __init__(self):
        DataTransferHeader.__init__(self,0xF1,0xD1,8)
        self.Speed1 = 0
        self.Speed2 = 0
        self.Speed3 = 0
        self.Speed4 = 0

    def __lshift__(self, Sender:QDataStream):
        self.Speed1 = Sender.readInt16()
        self.Speed2 = Sender.readInt16()
        self.Speed3 = Sender.readInt16()
        self.Speed4 = Sender.readInt16()

class Step_Motor_Control_Data(DataTransferHeader):
    def __init__(self):
        DataTransferHeader.__init__(self,0xF1,0xD3,12)
        self.AngleMotor1 = 0
        self.AngleMotor2 = 0
        self.AngleMotor3 = 0

        self.SpeedMotor1 = 0
        self.SpeedMotor2 = 0
        self.SpeedMotor3 = 0

    def __lshift__(self, Sender:QDataStream):
        self.AngleMotor1 = Sender.readInt16()
        self.AngleMotor2 = Sender.readInt16()
        self.AngleMotor3 = Sender.readInt16()

        self.SpeedMotor1 = Sender.readInt16()
        self.SpeedMotor2 = Sender.readInt16()
        self.SpeedMotor3 = Sender.readInt16()




class Accelerometer_Data(DataTransferHeader):
    def __init__(self):
        DataTransferHeader.__init__(self,0xF1,0xD2,12)
        self.AccelX = 0
        self.AccelY = 0
        self.AccelZ = 0

        self.AngularSpeedX = 0
        self.AngularSpeedY = 0
        self.AngularSpeedZ = 0

        self.Azimuth = 0
        self.Elevation = 0
        self.Pitch = 0

    def __lshift__(self, Sender:QDataStream):
        self.AccelX = Sender.readUInt16()
        self.AccelY = Sender.readUInt16()
        self.AccelZ = Sender.readUInt16()

        self.AngularSpeedX = Sender.readUInt16()
        self.AngularSpeedY = Sender.readUInt16()
        self.AngularSpeedZ = Sender.readUInt16()

        #self.Azimuth = Sender.readUInt16()
        #self.Elevation = Sender.readUInt16()
        #self.Pitch = Sender.readUInt16()
        #print("ACCEL - ",self.AccelX,self.AccelY,self.AccelZ)



class ConnectCheckRequest(DataTransferHeader):
    def __init__(self):
        DataTransferHeader.__init__(self,0xF1,0xC1,7)
        self.Connect = 0
        self.MESSAGE_SIZE = self.UNIT_SIZE


    def __lshift__(self, Sender:QDataStream):
        self.Connect = Sender.readInt8()
        print("CONNECT CHECK REQUEST LOAD FROM DATA STREAM")

    def __rshift__(self, Sender:QDataStream):
        Sender.writeInt16(self.HEADER_B1)
        Sender.writeInt16(self.HEADER_B2)
        Sender.writeInt16(self.UNIT_SIZE)
        Sender.writeInt8(self.Connect)


