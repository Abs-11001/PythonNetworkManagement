import sys

from loginWindow import login
from PyQt5.QtWidgets import QApplication,QMainWindow



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = login(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())


