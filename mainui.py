# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pictures/Neo_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 449, 781, 101))
        self.groupBox.setObjectName("groupBox")
        self.Serialtext = QtWidgets.QTextEdit(self.groupBox)
        self.Serialtext.setGeometry(QtCore.QRect(10, 30, 431, 61))
        self.Serialtext.setObjectName("Serialtext")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(460, 30, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(460, 62, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = matplotlibwidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 571, 401))
        self.widget.setObjectName("widget")
        self.verticalSlider_0 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_0.setGeometry(QtCore.QRect(620, 20, 22, 361))
        self.verticalSlider_0.setMaximum(100)
        self.verticalSlider_0.setProperty("value", 0)
        self.verticalSlider_0.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_0.setObjectName("verticalSlider_0")
        self.verticalSlider_1 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_1.setGeometry(QtCore.QRect(660, 20, 22, 361))
        self.verticalSlider_1.setMaximum(100)
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setObjectName("verticalSlider_1")
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(700, 20, 22, 361))
        self.verticalSlider_2.setMaximum(100)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setGeometry(QtCore.QRect(740, 20, 22, 361))
        self.verticalSlider_3.setMaximum(100)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setInvertedAppearance(False)
        self.verticalSlider_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_3.setTickInterval(10)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(620, 400, 151, 21))
        self.progressBar.setStatusTip("")
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStatusTip("")
        self.statusbar.setWhatsThis("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NEO_GUI_pannel V0.2"))
        self.groupBox.setTitle(_translate("MainWindow", "Serial baud rate = 115,200"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))

from testbed import matplotlibwidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

