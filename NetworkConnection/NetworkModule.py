#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PySide2 import QtCore
from PySide2.QtCore import QBuffer,QDataStream,QByteArray
from PySide2.QtNetwork import QTcpSocket
from PySide2.QtWidgets import QWidget
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

    def PrintData(self,DataString:str):
        self.ui.listWidgetRecieveData.addItem(DataString)
        #if self.ui.listWidgetRecieveData.count() == 5:
        #    self.ui.listWidgetRecieveData.clear()
        return 0



class NetworkConnectionClass(QtCore.QObject):
    SignalDataRec = Signal(str)
    SignalFrameDataAvailable = Signal()
    def __init__(self,parent=None):
        super(NetworkConnectionClass,self).__init__(parent=parent)
        self.CommandSocket = QTcpSocket()
        self.CommandSocket.connected.connect(self.EventConnectedHandle)
        self.CommandSocket.readyRead.connect(self.RecieveData)
        self.CommandSocket.connectToHost("192.168.100.5",2323)
        #self.CommandSocket.connectToHost("192.168.20.196",2323)

        self.Display = WindowNetworkConnection()

        self.NetworkDataArray = QByteArray()
        self.NetworkDataArray.resize(140)
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



        self.BufferRead.seek(0)
        self.BufferWrite.seek(0)

        self.LimitBufferSize = 100
        self.MinTransferUnit = 8
        self.MaxTransferUnit = 18
        self.bytesAvailable = 0


#        TestMessage = QByteArray(bytearray.fromhex('A1 A2 A3')); TestMessage2 = QByteArray(bytearray.fromhex('A4 A5 A6'))
#        self.BufferWriteQueue.write(TestMessage); self.BufferWriteQueue.write(TestMessage2)
#        print("BUFFER - ",self.NetworkDataArray)
#        self.Message = MessageData()
#        self.Message << self.NetworkDataStream << self.NetworkDataStream
    def __rshift__(self, Reciever:DataTransferHeader):
            #print("     READ BUFFER POS - ",self.BufferRead.pos())
        Reciever << self.ReadDataStream
        self.bytesAvailable -= Reciever.UNIT_SIZE

        if not self.BufferRead.pos() < self.LimitBufferSize - self.MaxTransferUnit:
                #print("READ BUFFER SEEK TO 0 - ",self.BufferRead.pos())
                self.BufferRead.seek(0)

        return self


    def EventConnectedHandle(self):
        self.SignalDataRec.emit("CONNECTED TO HOST")
        #self.SignalDataRec.emit("192.168.100.5 PORT 2323")
        self.SignalDataRec.emit("192.168.20.196 PORT 2323")
        #self.SignalDataRec.emit("BYTES IN REC BUFFER - " + str(self.bytesAvailable))

    def RecieveData(self):
        HEADER = QByteArray(); HEADER.resize(2)
        if self.bytesAvailable < self.LimitBufferSize - self.MaxTransferUnit:
            if self.BufferWrite.pos() < self.LimitBufferSize - self.MaxTransferUnit:
                newData = self.CommandSocket.read(self.LimitBufferSize - self.bytesAvailable)
                #print("NEW DATA - ",newData,"to POS - ",self.BufferWrite.pos())
                self.BufferWrite.write(newData)
                self.bytesAvailable += newData.size()

            else:
                H1 = 0
                H2 = 0
                while self.CommandSocket.bytesAvailable() > 0:
                    H1 = H2
                    H2 = self.SocketDataStream.readInt16()

                    if H1 == 0xF1 and (H2 == 0xD1 or H2 == 0xD2 or H2 == 0xD3):
                        self.BufferWrite.seek(0)
                        newData = self.CommandSocket.read(self.LimitBufferSize - self.bytesAvailable)
                        self.WriteDataStream.writeInt16(H1)
                        self.WriteDataStream.writeInt16(H2)
                            #print("==============================================================")
                            #print("SEEK TO 0")
                            #print("NEW DATA - ",newData,"to POS - ",self.BufferWrite.pos() - 4)
                        self.BufferWrite.write(newData)
                        self.bytesAvailable += (4 + newData.size())
                            #print("BUFFER - ",self.NetworkDataArray)
                        break
                    else:
                        self.WriteDataStream.writeInt16(H2)
                        self.bytesAvailable += 1


        #self.SignalDataRec.emit("BYTES IN REC BUFFER - " + str(self.bytesAvailable))

        if(self.bytesAvailable >= self.MinTransferUnit):
            self.SignalFrameDataAvailable.emit()




    def HandleErrorSocket(self):
        print("ErrorSocket")


