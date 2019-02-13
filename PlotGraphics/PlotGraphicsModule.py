from __future__ import unicode_literals
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QBrush,QColor,QPen,QPainter

import math
import sys
import os
import random
import matplotlib
from GroupGraphPlot import Ui_GroupGraphWindow

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PySide2 import QtCore, QtWidgets

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class LineGraphicsPlot(QtCharts.QChart):
    def __init__(self):
        super(LineGraphicsPlot, self).__init__()
        self.DataSeries = QtCharts.QSplineSeries()
        self.Area = QtCharts.QAreaSeries(self.DataSeries)
        self.Area.setBrush(QBrush(QColor(200,100,224,40)))



        #self.addSeries(self.DataSeries)
        self.addSeries(self.Area)

        self.AxisX = QtCharts.QValueAxis()
        self.AxisY = QtCharts.QValueAxis()
        self.addAxis(self.AxisX,QtCore.Qt.AlignBottom)
        self.addAxis(self.AxisY,QtCore.Qt.AlignLeft)
        #self.DataSeries.attachAxis(self.AxisX)
        #self.DataSeries.attachAxis(self.AxisY)

        self.Area.attachAxis(self.AxisX)
        self.Area.attachAxis(self.AxisY)

        self.AxisX.setTickCount(5)

        self.mx = 0
        self.my = 0
        self.AxisX.setRange(self.mx,self.mx + 5)
        self.AxisY.setRange(-1.2,1.2)
        self.legend().hide()
        self.axisX().hide()

        self.setTheme(QtCharts.QChart.ChartThemeDark)

        #self.setTheme(QtCharts.QChart.ChartThemeBrownSand)
        #self.setTheme(QtCharts.QChart.ChartThemeHighContrast)
        self.setPlotAreaBackgroundBrush(QBrush(QColor(200,100,14)))



        self.m_timer = QtCore.QTimer(self)
        self.m_timer.timeout.connect(self.handleTimeout)
        self.m_timer.start(25)

    def handleTimeout(self):
        self.mx += 0.1
        self.my = math.sin(self.mx)
        self.DataSeries.append(self.mx, self.my)

        if self.DataSeries.count() == 50:
            self.AxisX.setRange(self.mx - 5,self.mx)
            self.DataSeries.remove(0)

        if self.mx == 1000:
            self.m_timer.stop()



class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class MyDynamicMplCanvas(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        super(MyDynamicMplCanvas, self).__init__(*args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(35)
        self.MyTime = arange(0.0, 30.0, 0.02)
        self.MySine = sin(2 * pi * self.MyTime)
        self.Pos = 0
        self.line, = self.axes.plot(self.MyTime[0 + self.Pos:50 + self.Pos], self.MySine[0 + self.Pos:50 + self.Pos])
        self.line.set_xdata(self.MyTime[self.Pos:50 + self.Pos])
        #self.compute_initial_figure()

    def compute_initial_figure(self):
        self.draw()

    def update_figure(self):
        self.Pos += 1
        self.line.set_ydata(self.MySine[self.Pos:50 + self.Pos])

        self.axes.draw_artist(self.axes.patch)
        self.axes.draw_artist(self.line)
        self.fig.canvas.update()
        self.fig.canvas.flush_events()

        if self.Pos > 1000:
            self.Pos = 0


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        dc1 = MyDynamicMplCanvas(self.main_widget, width=3, height=3, dpi=80)
        dc2 = MyDynamicMplCanvas(self.main_widget, width=3, height=3, dpi=80)
        dc3 = MyDynamicMplCanvas(self.main_widget, width=3, height=3, dpi=80)
        dc4 = MyDynamicMplCanvas(self.main_widget, width=3, height=3, dpi=80)
        l.addWidget(dc1)
        l.addWidget(dc2)
        l.addWidget(dc3)
        l.addWidget(dc4)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)


class GroupWindowModule(QtWidgets.QWidget):
    #SignalFire = QtCore.pyqtSignal()
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_GroupGraphWindow()
        self.ui.setupUi(self)
        self.Pos = 0

    def addWidget(self,Widget):
        if self.Pos == 0:
            self.ui.verticalLayout.addWidget(Widget)
        if self.Pos == 1:
            self.ui.verticalLayout_2.addWidget(Widget)
        if self.Pos == 2:
            self.ui.verticalLayout_3.addWidget(Widget)
        if self.Pos == 3:
            self.ui.verticalLayout_4.addWidget(Widget)
        self.Pos += 1
        return 0
