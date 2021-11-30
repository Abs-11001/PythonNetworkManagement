import sys

from PyQt5 import QtGui
from loginWindow import login
import requests
import threading
from PyQt5.QtWidgets import QApplication,QMainWindow



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = login(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())


