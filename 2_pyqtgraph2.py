import pyqtgraph as pg
import numpy as np
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        pg.setConfigOptions(background='w', foreground='b')  # 배경 흰색으로.. ; global configuration options

        x = np.arange(20)
        y = np.linspace(0, 20, num=20)

        pw = pg.PlotWidget()
        pw.showGrid(x=True, y=True)

        pw.setXRange(0, 22, padding=0)   # padding=0  --> y축 공백 제거함.
        # pw.setYRange(0, 22, padding=0)   # padding=0  --> x축 공백 제거함.

        barchar = pg.BarGraphItem(x=x, height=y, width=0.6, brush='r')  # width = 막대 넓이
        # bar_chart = pg.BarGraphItem(x=x, width=0.9, height=y,  brush='r', pen='g')
        pw.addItem(barchar)

        layout = QHBoxLayout()
        layout.addWidget(pw)
        self.setLayout(layout)

        self.setGeometry(300, 100, 550, 500)  # x, y, width, height
        self.setWindowTitle("pyqtgraph 예제 - bar chart")
        self.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())