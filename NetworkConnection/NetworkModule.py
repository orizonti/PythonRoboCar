#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PySide2 import QtCore
from PySide2.QtCore import QBuffer,QDataStream,QByteArray
from PySide2.QtNetwork import QTcpSocket, QUdpSocket, QHostAddress
from PySide2.QtCore import QIODevice
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QTime
from NetworkModuleUI import Ui_NetworkControl
from TransferDataObjects import *
from PySide2.QtCore import QObject, Signal, Slot



#=========SIGNALS===================
#closed = pyqtSignal()
# This defines a signal called 'rangeChanged' that takes two
# integer arguments.
#range_changed = pyqtSignal(int, int, name='rangeChanged')

class WindowNetworkConnection(QWidget):
    #SignalFire = QtCore.pyqtSignal()
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.ui = Ui_NetworkControl()
        self.ui.setupUi(self)

    def PrintData(self,DataString:str,Channel:int):

        print("PRINT DATA NETWORK CHANNEL - ", Channel)
        if Channel == 0:
            self.ui.listWidgetRecieveData.addItem(DataString)
        if Channel == 1:
            self.ui.listWidgetSendData.addItem(DataString)
        #if self.ui.listWidgetRecieveData.count() == 5:
        #    self.ui.listWidgetRecieveData.clear()
        return 0



class NetworkConnectionClass(QtCore.QObject):
    SignalDataRec = Signal(str,int)
    SignalFrameDataAvailable = Signal()
    def __init__(self,parent=None):
        super(NetworkConnectionClass,self).__init__(parent=parent)
        #self.CommandSocket = QTcpSocket()
        self.CommandSocket = QUdpSocket()
        self.CommandSocket.bind(QHostAddress("192.168.100.2"),2323)
        self.CommandSocket.connected.connect(self.EventConnectedHandle)
        self.CommandSocket.readyRead.connect(self.RecieveData)

        #self.CommandSocket.connectToHost("192.168.100.5",2323,QIODevice.ReadWrite)
        #self.CommandSocket.connectToHost("127.0.0.1",2323,QIODevice.ReadWrite)
        #self.CommandSocket.connectToHost("192.168.20.196",2323,QIODevice.ReadWrite)
        #print("NETWORK - ",self.CommandSocket.localAddress(),self.CommandSocket.peerAddress())

        self.Display = WindowNetworkConnection()

        self.NetworkDataArray = QByteArray()
        self.NetworkDataArray.resize(2000)
        self.SignalDataRec.connect(self.Display.PrintData)

        self.BufferWrite = QBuffer(self.NetworkDataArray)
        self.BufferWrite.open(QBuffer.WriteOnly)

        self.BufferRead = QBuffer(self.NetworkDataArray)
        self.BufferRead.open(QBuffer.ReadOnly)

        self.ReadDataStream = QDataStream(self.BufferRead)
        self.ReadDataStream.setByteOrder(QDataStream.LittleEndian)

        self.WriteDataStream = QDataStream(self.BufferWrite)
        self.WriteDataStream.setByteOrder(QDataStream.LittleEndian)

        self.SocketDataStream = QDataStream(self.CommandSocket)
        self.SocketDataStream.setByteOrder(QDataStream.LittleEndian)

        self.Timer = QTime()
        self.Timer.start()


        self.BufferRead.seek(0)
        self.BufferWrite.seek(0)

        self.LimitBufferSize = 2000
        self.MinTransferUnit = 7
        self.MaxTransferUnit = 18
        self.bytesAvailable = 0
        self.Display.ui.pushButton.clicked.connect(self.SendData)

        #===================================================== WRITE BUFFER
        self.SendBuffer = QByteArray()

        #=====================================================

#        TestMessage = QByteArray(bytearray.fromhex('A1 A2 A3')); TestMessage2 = QByteArray(bytearray.fromhex('A4 A5 A6'))
#        self.BufferWriteQueue.write(TestMessage); self.BufferWriteQueue.write(TestMessage2)
#        print("BUFFER - ",self.NetworkDataArray)
#        self.Message = MessageData()
#        self.Message << self.NetworkDataStream << self.NetworkDataStream
    def __rshift__(self, Reciever:DataTransferHeader):
        Reciever << self.ReadDataStream
        self.bytesAvailable -= Reciever.UNIT_SIZE
        print("BYTES AVAILABLE - ",self.bytesAvailable)
        #print("     REABUFFER POS - ",self.BufferRead.pos(),'BYTES AVAILABLE - ',self.bytesAvailable,"UNIT SIZE -",Reciever.UNIT_SIZE)
        #print("   READ UNIT -",Reciever.UNIT_SIZE)
        #print("   READ BUFFER POS -",self.BufferRead.pos())
        #print("   READ BUFFER -",self.BufferRead.data().toHex())

        if not self.BufferRead.pos() < self.LimitBufferSize - self.MaxTransferUnit:
                self.BufferRead.seek(0)
                print("READ BUFFER SEEK TO 0 - ",self.BufferRead.pos())

        return self


    def EventConnectedHandle(self):
        self.SignalDataRec.emit("CONNECTED TO HOST",0)
        #self.SignalDataRec.emit("192.168.100.5 PORT 2323",0)
        self.SignalDataRec.emit("192.168.20.197 PORT 2323",0)
        #self.SignalDataRec.emit("BYTES IN REC BUFFER - " + str(self.bytesAvailable))

    def RecieveData(self):
        #self.CommandSocket.receiveDatagram(20)
        HEADER = QByteArray(); HEADER.resize(2)
        if self.bytesAvailable < self.LimitBufferSize - self.MaxTransferUnit:   #check that memory for packet available
            if self.BufferWrite.pos() < self.LimitBufferSize - self.MaxTransferUnit:
                (newData,sender,senderPort) = self.CommandSocket.readDatagram(20)

                #newData = self.CommandSocket.read(self.LimitBufferSize - self.bytesAvailable)
                #print("   NEW DATA - ",newData.toHex(),"to POS - ",self.BufferWrite.pos())
                self.BufferWrite.write(newData)
                self.bytesAvailable += newData.size()
                print(self.Timer.restart())
                #print("REC ",data)
                #print("   BUFFER - ",self.BufferWrite.data().toHex())

            else:
                H1 = 0
                H2 = 0
                while self.CommandSocket.bytesAvailable() > 0:
                    H1 = H2
                    H2 = self.SocketDataStream.readInt16()

                    if H1 == 0xF1 and (H2 == 0xD1 or H2 == 0xD2 or H2 == 0xD3 or H2 == 0xC1):
                        self.BufferWrite.seek(0)
                        newData = self.CommandSocket.read(self.LimitBufferSize - self.bytesAvailable)
                        self.WriteDataStream.writeInt16(H1)
                        self.WriteDataStream.writeInt16(H2)
                        print("==============================================================")
                        print("SEEK TO 0")
                        print("NEW DATA - ",newData,"to POS - ",self.BufferWrite.pos() - 4)
                        self.BufferWrite.write(newData)
                        self.bytesAvailable += (4 + newData.size())
                        #print("BUFFER - ",self.NetworkDataArray.toHex())
                        break
                    else:
                        self.WriteDataStream.writeInt16(H2)
                        self.bytesAvailable += 1


        #self.SignalDataRec.emit("BYTES IN REC BUFFER - " + str(self.bytesAvailable))

        if(self.bytesAvailable >= self.MinTransferUnit):
            self.SignalFrameDataAvailable.emit()
    def SendData(self):
        Req = ConnectCheckRequest()
        self.SendBuffer.clear()
        self.SendBuffer.resize(Req.MESSAGE_SIZE)

        WriteDataStream = QDataStream(self.SendBuffer,QIODevice.ReadWrite)
        WriteDataStream.setByteOrder(QDataStream.LittleEndian)
        Req >> WriteDataStream


        self.CommandSocket.write(self.SendBuffer)
        self.CommandSocket.waitForBytesWritten(20)
        self.SignalDataRec.emit("CHECK CONNECT - " + str(Req.Connect),1)

        #self.CommandSocket.write(bytearray(b'TestMessage\r\n'))
        #print("WRITE BUFFER - ",self.SendBuffer.toHex())
        #print("===============================================")




    def HandleErrorSocket(self):
        print("ErrorSocket")


