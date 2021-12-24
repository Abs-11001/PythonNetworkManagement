import sys

from loginWindow import LoginMainWindow,login
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = LoginMainWindow()
    ui = login(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())


