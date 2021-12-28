# coding=utf-8

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QWidget, QMessageBox
from PyQt5.QtCore import *

import assets.UI.loginWindowUi as loginWindowUi
import os, json
from chatWindow import ChatMainWindow,Chat
import webbrowser

def messageDialog(parentWidget, text):
    # 参考： https://www.cnblogs.com/leokale-zz/p/13106721.html
    msg_box = QMessageBox.critical(parentWidget, "警告", text, QMessageBox.Yes)

class LoginMainWindow(QMainWindow):
    # 检测键盘回车按键
    def keyPressEvent(self, event):
        pass

class Login(loginWindowUi.Ui_MainWindow):
    def __init__(self, mainWindow):
        super().setupUi(mainWindow)
        self.mainWindow = mainWindow
        self.mainWindow.setFocus()

        # 设置密码框输入模式为密码模式
        self.loginPsd.setEchoMode(QLineEdit.Password)

        # 设置登陆界面的头图
        topImageFile = QtGui.QPixmap('assets/imgs/topImage.jpg')
        self.topImage.setPixmap(topImageFile)
        self.topImage.setScaledContents(True)

        # 加载已保存的账号密码
        self.loadUserInfo()

        # 绑定checkbox选中
        self.rememberUser.stateChanged.connect(lambda: self.rememberUserClick())
        self.rememberPassword.stateChanged.connect(lambda: self.rememberPsdClick())

        # 绑定登陆点击
        self.loginBtn.clicked.connect(lambda: self.loginClick())

        # 绑定注册账号
        self.registerAccount.clicked.connect(lambda: self.openRegister())

    def loginClick(self):
        '''
        :param loginMainWindow: 登陆界面的 mainwindow，打开聊天界面后，用来关闭登陆界面
        :return:
        '''
        user = self.loginUser.text()
        psd = self.loginPsd.text()
        if user == "" or psd == "":
            messageDialog(self.mainWindow,"请填写账号或密码!")
            return

        info = {}
        try:
            with open("assets/config/account.json", "r", encoding='utf-8') as file:
                info = json.load(file)
                if user in info.keys():
                    if psd == info[user]['psd']:
                        user_name = info[user]['user_name']
                        print(user_name)
                        # 当验证通过后，判断是否勾选了保存密码
                        self.saveUserInfo()

                        # 先初始化聊天窗口的对象
                        self.chatMainWindow = ChatMainWindow()
                        self.chatWindow = Chat(self.chatMainWindow, user)

                        # 然后显示聊天界面并关闭登陆界面
                        self.chatMainWindow.show()
                        self.mainWindow.close()
                    else:
                        messageDialog(self.mainWindow, "账号或密码错误!")
                else:
                    messageDialog(self.mainWindow, "请先注册账号!")

        except:
            messageDialog(self.mainWindow, "请先注册账号!")

    def saveUserInfo(self):
        """
        保存账号密码，json格式
        checkState()返回值
        0：未选中
        2：选中
        :return:
        """

        path = "assets/config/"
        if not os.path.exists(path):
            os.mkdir(path)

        rememberUser = True if self.rememberUser.checkState() == 2 else False
        rememberPsd = True if self.rememberPassword.checkState() == 2 else False

        # 记住账号被勾选
        if rememberUser:
            with open(path + "user.json", "w") as file:
                user = {"user": self.loginUser.text(), "rememberUser": rememberUser, "rememberPsd": rememberPsd}
                json.dump(user, file)

        # 记住密码被勾选
        if rememberPsd:
            with open(path + "user.json","w") as file:
                user = {"user": self.loginUser.text(), "psd": self.loginPsd.text(), "rememberUser": rememberUser, "rememberPsd": rememberPsd}
                json.dump(user,file)

    def loadUserInfo(self):
        path = "assets/config/"
        try:
            with open(path + "user.json","r") as file:
                info = json.load(file)
                if "user" in info.keys():
                    user = info['user']
                    self.loginUser.setText(user)
                if "psd" in info.keys():
                    psd = info['psd']
                    self.loginPsd.setText(psd)
                if "rememberUser" in info.keys():
                    rememberUser = bool(info['rememberUser'])
                    self.rememberUser.setChecked(rememberUser)
                if "rememberPsd" in info.keys():
                    rememberPsd = bool(info['rememberPsd'])
                    self.rememberPassword.setChecked(rememberPsd)
        except Exception as e:
            print(e)
            print("只是一个简单的文件不存在报错，问题不大，别慌...")

    def rememberUserClick(self):
        rememberUser_state = self.rememberUser.checkState()
        if rememberUser_state == 0:
            self.rememberPassword.setChecked(False)

    def rememberPsdClick(self):
        rememberPsd_state = self.rememberPassword.checkState()
        if rememberPsd_state == 2:
            self.rememberUser.setChecked(True)

    def openRegister(self):
        registerUrl = "http://localhost:7878/register"
        try:
            webbrowser.get('chrome').open_new_tab(registerUrl)
        except Exception as e:
            webbrowser.open_new_tab(registerUrl)
