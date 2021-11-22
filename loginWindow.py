from PyQt5 import QtGui
import assets.UI.loginWindowUi as loginWindowUi
import requests
import threading
from PyQt5.QtWidgets import QApplication,QMainWindow

class login(loginWindowUi.Ui_MainWindow):
    def __init__(self,mainWindow):
        super().setupUi(mainWindow)
        self.pushButton.clicked.connect(lambda:self.loginClick(self.topImage))
        topImageFile = QtGui.QPixmap('assets/imgs/topImage.jpg')
        self.topImage.setPixmap(topImageFile)
        self.topImage.setScaledContents(True)
    def loginClick(self,topImage):
        # topImage.setText("fff")
        thread = threading.Thread(target=self.loginCount,args=(self.loginUser,))
        thread.start()

    def loginCount(self,loginUser):
        res = requests.get("http://www.flask.waheng.fun:7878/checkIn?qq=" + loginUser.text())
        print(res.text)