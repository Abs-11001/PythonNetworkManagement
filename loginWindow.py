from PyQt5 import QtGui
import assets.UI.loginWindowUi as loginWindowUi
import assets.UI.chatWindowUi as chatWindowUi
from PyQt5.QtWidgets import QApplication, QMainWindow


class login(loginWindowUi.Ui_MainWindow):
    def __init__(self, mainWindow):
        super().setupUi(mainWindow)

        # 先初始化聊天窗口的对象
        self.chatMainWindow = QMainWindow()
        self.chatWindow = chat(self.chatMainWindow)

        # 设置登陆界面的头图
        topImageFile = QtGui.QPixmap('assets/imgs/topImage.jpg')
        self.topImage.setPixmap(topImageFile)
        self.topImage.setScaledContents(True)

        # 绑定登陆点击
        self.loginBtn.clicked.connect(lambda: self.loginClick(mainWindow))

    def loginClick(self, loginMainWindow):
        '''
        :param loginMainWindow: 登陆界面的 mainwindow，用来关闭登陆界面
        :return:
        '''
        user = self.loginUser.text()
        psd = self.loginPsd.text()

        if user == "123" and psd == "123":
            # 当验证通过之后就显示聊天界面并关闭登陆界面
            self.chatMainWindow.show()
            loginMainWindow.close()


class chat(chatWindowUi.Ui_MainWindow):
    def __init__(self, mainWindow):
        super().setupUi(mainWindow)

