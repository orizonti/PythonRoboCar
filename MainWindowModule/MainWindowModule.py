import sys
import PySide2
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtWidgets import QGraphicsProxyWidget
from MainWindowContainer import Ui_MainWindowContainer

#class GraphicsWidgetNode(QGraphicsProxyWidget):
#    def __init__(self,parent=None):
#        QGraphicsProxyWidget.__init__(self,parent)
#        print("asdfsad")

class MainWindowClass(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.ui = Ui_MainWindowContainer()
        self.ui.setupUi(self)

        self.WindowWidth = 1000
        self.WindowHeight = 1000

        self.GraphicsSceneCont = QGraphicsScene()
        self.GraphicsSceneCont.setSceneRect(0,0,self.WindowWidth,self.WindowHeight)
        self.ui.graphicsView.setScene(self.GraphicsSceneCont)

    def SetModuleWidget(self,x,y,WindowModule):
        Widget =  QGraphicsProxyWidget()
        Widget.setWidget(WindowModule)
        Widget.setWindowFlags(Qt.Window)
        Widget.setPos(x,y)
        Widget.setFlag(PySide2.QtWidgets.QGraphicsItem.ItemIsMovable,True)
        Widget.setFlag(PySide2.QtWidgets.QGraphicsItem.ItemIsSelectable,True)
        self.GraphicsSceneCont.addItem(Widget)

    def SetWindowItem(self,x,y,WindowModule):
        WindowModule.setPos(x,y)
        WindowModule.resize(250,250)
        #WindowModule.setWindowFlags(Qt.Window)
        WindowModule.setFlag(PySide2.QtWidgets.QGraphicsItem.ItemIsMovable,True)
        WindowModule.setFlag(PySide2.QtWidgets.QGraphicsItem.ItemIsSelectable,True)
        self.GraphicsSceneCont.addItem(WindowModule)








