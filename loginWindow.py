from PyQt5 import QtGui,QtWidgets,QtCore

import assets.UI.loginWindowUi as loginWindowUi
import assets.UI.chatWindowUi as chatWindowUi
from PyQt5.QtWidgets import QApplication, QMainWindow
import os

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

        # 保存账号密码
        self.savePassword.clicked.connect(lambda: self.saveInfo(mainWindow))



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

    def saveInfo(self,loginMainWindow):
        if not os.path.exists("assets/config/"):
            os.mkdir("assets/config/")




class chat(chatWindowUi.Ui_MainWindow):
    def __init__(self, mainWindow):
        super().setupUi(mainWindow)

        # 设置添加联系人按钮
        self.add_btn.setIcon(QtGui.QIcon("assets/imgs/icon/add.svg"))

        # 聊天界面刚加载进去的时候是不显示任何东西的，用一个标志来标识是否有联系人被点击了，如果点击了才会显示出来右侧界面
        self.clickEdFlag = False

        # 取消macos 自带的部件晕圈效果（一个蓝色的边框）
        self.searchOradd.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.listWidget.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)

        self.listWidget.addItem("柏乐佳")
        self.listWidget.addItem("朱石磊")
        # 绑定listWidget点击函数
        self.listWidget.itemClicked.connect(self.listItemClicked)

        # 设置聊天输入框不可用
        self.textEdit.setVisible(False)

        # # 取消添加好友输入框自动获取焦点
        self.searchOradd.clearFocus()

    def listItemClicked(self,index):
        itemName = self.listWidget.item(self.listWidget.row(index)).text()
        self.titleName.setText(itemName)
        # 如果是第一次点击联系人的话就加载基本图标
        if not self.clickEdFlag:
            # 加载基本样式
            self.widget_2.setStyleSheet("#widget_3,#widget_4,#widget_5{\n"
                                        "    border-bottom: 1.5px solid #DCDCDC;\n"
                                        "    background-color: #F1F1F1;\n"
                                        "}"
                                        "#widget_6{\n"
                                        "    background-color: #F1F1F1;\n"
                                        "}")
            self.widget_5.setStyleSheet("#textEdit{\n"
                                        "    background-color: #F1F1F1;\n"
                                        "   border: none;\n"
                                        "}")
            self.widget_6.setStyleSheet("QPushButton{\n"
                                        "    border:none;\n"
                                        "    background-color:#F1F1F1;\n"
                                        "}")
            # 初始化基本图标
            self.send_emoji_btn.setIcon(QtGui.QIcon("assets/imgs/icon/smile.svg"))
            self.send_file_btn.setIcon(QtGui.QIcon("assets/imgs/icon/file.svg"))
            self.look_history_btn.setIcon(QtGui.QIcon("assets/imgs/icon/history.svg"))
            self.clickEdFlag = True

            # 解封聊天输入框
            self.textEdit.setVisible(True)

            # 封印文字logo
            self.label.setVisible(False)


