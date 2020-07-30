
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

# Serial msg constant
WIN_WIDTH, WIN_HEIGHT = 355, 200  # Window size (original = 684, 400)
SER_TIMEOUT = 0.1  # Timeout for serial Rx
RETURN_CHAR = "\n"  # Char to be sent when Enter key pressed
PASTE_CHAR = "\x16"  # Ctrl code for clipboard paste
baudrate = 115200  # Default baud rate
portname = "COM4"  # Default port name
hexmode = True  # Flag to enable hex display

# Global array for Serial Rx msg
rx_msg = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
msg_idx = 0

# load main UI from Qt designer
form_class = uic.loadUiType("main.ui")[0]

# Convert a string to bytes
def str_bytes(s):
    return s.encode('latin-1')

# Convert bytes to string
def bytes_str(d):
    return d if type(d) is str else "".join([chr(b) for b in d])

# Return hexadecimal values of data
def hexdump(data):
    return " ".join(["%02X" % ord(b) for b in data])

# Return a string with high-bit chars replaced by hex values
def textdump(data):
    return "".join(["[%02X]" % ord(b) if b > '\x7e' else b for b in data])

# Display incoming serial data
def display(s):
    if not hexmode:
        sys.stdout.write(textdump(str(s)))
    else:
        sys.stdout.write(hexdump(s) + ' ')

# Main widget
class MyWidget(Ui_MainWindow, QWidget):
    text_update = QtCore.pyqtSignal(str)

    def __init__(self, *args):

        # Main UI setup
        self.setupUi(MainWindow)
        QWidget.__init__(self, *args)
        self.text_update.connect(self.append_text)  # Connect text update to handler
        sys.stdout = self  # Redirect sys.stdout to self
        self.serth = SerialThread(portname, baudrate)  # Start serial thread
        self.serth.start()

    def write(self, text):  # Handle sys.stdout.write: update display
        self.text_update.emit(text)  # Send signal to synchronise call with main thread

    def flush(self):  # Handle sys.stdout.flush: do nothing
        pass

    def append_text(self, text):  # Text display update handler
        cur = self.Serialtext.textCursor()
        cur.movePosition(QtGui.QTextCursor.End)  # Move cursor to end of text
        s = str(text)
        while s:
            head, sep, s = s.partition("\n")  # Split line at LF
            cur.insertText(head)  # Insert text at cursor
            if sep:  # New line if LF
                cur.insertBlock()
        self.Serialtext.setTextCursor(cur)  # Update visible cursor

    def keypress_handler(self, event):  # Handle keypress from text box
        k = event.key()
        s = RETURN_CHAR if k == QtCore.Qt.Key_Return else event.text()
        if len(s) > 0 and s[0] == PASTE_CHAR:  # Detect ctrl-V paste
            cb = QApplication.clipboard()
            self.serth.ser_out(cb.text())  # Send paste string to serial driver
        else:
            self.serth.ser_out(s)  # ..or send keystroke

    def closeEvent(self, event):  # Window closing
        self.serth.running = False  # Wait until serial thread terminates
        self.serth.wait()


# Thread to handle incoming &amp; outgoing serial data
class SerialThread(QtCore.QThread):
    def __init__(self, portname, baudrate):  # Initialise with serial port details
        QtCore.QThread.__init__(self)
        self.portname, self.baudrate = portname, baudrate
        self.txq = Queue.Queue()
        self.running = True

    def ser_out(self, s):  # Write outgoing data to serial port if open
        self.txq.put(s)  # ..using a queue to sync with reader thread

    def ser_in(self, s):  # Write incoming serial data to screen
        display(s)

    def run(self):  # Run serial reader thread
        global rx_msg
        global msg_idx

        print("Opening %s at %u baud %s" % (self.portname, self.baudrate,
                                            "(hex display)" if hexmode else ""))

        try:
            self.ser = serial.Serial(self.portname, self.baudrate, timeout=SER_TIMEOUT)
            time.sleep(SER_TIMEOUT * 1.2)
            self.ser.flushInput()
        except:
            self.ser = None
        if not self.ser:
            print("Can't open port")
            self.running = False
        while self.running:
            s = self.ser.read(1)    # Neo : parameter "1" means 1byte
            s2 = int.from_bytes(s, "big")

            #s = self.ser.read(self.ser.in_waiting or 1)
            # Neo : parameter "self.ser.in_waiting" ?
            if s:  # Get data from serial port
                #self.ser_in(bytes_str(s))  # ..and convert to string
                if s == b'#': #0x23, "#", header
                    msg_idx = 0
                else:
                    msg_idx += 1
                rx_msg[msg_idx] = s2
                if s == b'*': #0x2A, "*", tail
                    #ui.Serialtext_2.append("1")
                    print(rx_msg)
                # Neo : in this point, serial 16byte string observed.
            if not self.txq.empty():
                txd = str(self.txq.get())  # If Tx data in queue, write to serial port
                self.ser.write(str_bytes(txd))
        if self.ser:  # Close serial port when thread finished
            self.ser.close()
            self.ser = None

# Thread test
class Thread_0(QtCore.QThread):

    def __init__(self):
        # super().__init__(self)
        QtCore.QThread.__init__(self)
        self.val_0 = 0
        # connect slider and progress bar
        ui.verticalSlider_3.valueChanged.connect(ui.progressBar.setValue)

    def run(self):
        while True:
            print(self.val_0)
            self.val_0 += 1
            time.sleep(0.5)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    print("App started")

    MainWindow = QtWidgets.QMainWindow()
    ui = MyWidget()
    MainWindow.show()

    test_0 = Thread_0()
    test_0.start()

    sys.exit(app.exec_())

# EOF