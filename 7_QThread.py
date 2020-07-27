
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QTextEdit, QWidget, QApplication, QVBoxLayout, QMainWindow, QHBoxLayout
from PyQt5 import uic

from mainui import Ui_MainWindow

try:
    import Queue
except:
    import queue as Queue
import sys, time, serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# Thread test
class Thread_0(QtCore.QThread):

    def __init__(self):
        # super().__init__(self)
        QtCore.QThread.__init__(self)
        self.val_0 = 0

    def run(self):
        while True:
            print(self.val_0)
            self.val_0 +=1
            time.sleep(5)

# Thread test
class Thread_1 (QtCore.QThread):

    def __init__(self):
        # super().__init__(self)
        QtCore.QThread.__init__(self)
        self.val_1 = 5555

    def run(self):
        while True:
            print(self.val_1)
            time.sleep(0.5)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    print("App started")

    test_0 = Thread_0()
    test_1 = Thread_1()
    test_0.start()
    test_1.start()

    sys.exit(app.exec_())

# EOF