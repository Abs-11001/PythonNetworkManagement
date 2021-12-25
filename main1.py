# coding=utf-8

import sys

from loginWindow import LoginMainWindow, Login
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = LoginMainWindow()
    ui = Login(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())


