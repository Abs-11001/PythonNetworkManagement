import assets.UI.chatWindowUi as chatWindowUi

from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QMainWindow,QLineEdit, QApplication, QWidget
from PyQt5.QtCore import *

import socket,json,struct

class ChatMainWindow(QMainWindow):
    # 检测键盘回车按键
    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Enter):
            print('测试：Enter')


class chat(chatWindowUi.Ui_MainWindow):
    def __init__(self, mainWindow):
        super().setupUi(mainWindow)

        # 任意一个控件获取焦点，这样输入框就失去焦点了
        self.widget.setFocus()

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
        self.msgContainer.setVisible(False)
        # 设置发送消息按钮不可用
        self.sendMsg_btn.setVisible(False)

        # 绑定发送消息按钮函数
        self.sendMsg_btn.clicked.connect(self.sendMsgClicked)

        # 创建tcp
        # 客户端

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('connecting to server...')
        self.sock.connect(('127.0.0.1', 8000))
        print('my address is ', self.sock.getsockname())



    def listItemClicked(self,index):
        itemName = self.listWidget.item(self.listWidget.row(index)).text()
        self.chatObject.setText(itemName)
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
            self.widget_5.setStyleSheet("#msgContainer{\n"
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
            self.msgContainer.setVisible(True)
            # 解封发送消息按钮
            self.sendMsg_btn.setVisible(True)

            # 封印文字logo
            self.label.setVisible(False)


    def sendMsgClicked(self):
        print("发送消息按钮被点击")
        msg = self.msgContainer.toPlainText().encode('utf-8')
        to = self.chatObject.text()

        header = {
            'type': 'msg',
            'size': len(msg),
            'to': to
        }
        header_json = json.dumps(header).encode('utf-8')
        header_json_len = len(header_json)
        print(header_json_len)
        # 告诉服务器我的json数据有多大
        self.sock.send(struct.pack("i",header_json_len))
        # 告诉服务器我的json数据，里面包含了一些信息
        self.sock.send(header_json)
        # 告诉服务器我的msg数据
        self.sock.sendall(msg)

