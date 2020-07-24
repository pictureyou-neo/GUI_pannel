from PyQt5 import QtGui, QtCore, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MplCanvas(FigureCanvas):

    def __init__(self):
        # Bar graph by matplot constant
        N = 5
        value = (20, 50, 30, 35, 27)
        ind = np.arange(N)
        width = 0.35

        # Bar graph draw
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.bar(ind, value, width)
        self.ax.set_xticks(ind + width / 20)
        self.ax.set_xticklabels(['G1', 'G2', 'G3', 'G4', 'G5'])
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class matplotlibwidget(QtWidgets.QWidget):

    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
