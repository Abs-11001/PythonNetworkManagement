# coding=utf-8

import json
import os
import socket
import struct
import threading
from datetime import datetime

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor, QColor
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog

import assets.UI.chatWindowUi as chatWindowUi

class ChatMainWindow(QMainWindow):
    # 检测键盘回车按键
    def keyPressEvent(self, event):
        pass
        # if (event.key() == Qt.Key_Enter):
        #     print('测试：Enter')


class Chat(chatWindowUi.Ui_MainWindow):
    def __init__(self, mainWindow, user):
        super().setupUi(mainWindow)
        self.mainWindow = mainWindow
        # 保存当前客户端用户
        self.user = user
        # 保存申请添加好友的人
        self.from_user = ""
        self.fileJson = ""
        mainWindow.setWindowTitle(user)

        # 任意一个控件获取焦点，这样输入框就失去焦点了
        self.widget.setFocus()

        # 聊天界面刚加载进去的时候是不显示任何东西的，用一个标志来标识是否有联系人被点击了，如果点击了才会显示出来右侧界面
        self.clickEdFlag = False
        # 是否显示emoji容器标志
        self.showEmojiFlag = False
        # 是否存在待发送文件
        self.sendFileFlag = False

        # **********************************
        # 设置部分控件显示状态
        self.initElements()
        # **********************************
        # 初始化槽与信号
        self.initSlotSignal()
        # **********************************

        # 加载好友列表
        self.loadFriendList()

        # 创建tcp  客户端
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print('connecting to server...')
            self.sock.connect(('127.0.0.1', 8000))
            print('my address is ', self.sock.getsockname())
            t = threading.Thread(target=self.recvAll, args=(self.sock,))
            t.start()
        except:
            print("服务器连接失败")

    def listItemClicked(self, index):
        itemName = self.listWidget.item(self.listWidget.row(index)).text()
        self.chatObject.setText(itemName)

        # 加载聊天记录
        self.loadChatRecord(self.user, self.chatObject.text())

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
            self.widget_4.setStyleSheet("#chatShow{\n"
                                        "   border: none;\n"
                                        "   border-bottom: 1.5px solid #DCDCDC;\n"
                                        "	background-color:  #F1F1F1;\n"
                                        "}\n"
                                        "#emoji_container{\n"
                                        "   border: 1px solid black;\n"
                                        "   border-radius: 10px;\n"
                                        "   background-color: #F1F1F1;\n"
                                        "}\n")
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
        from_user = self.user
        to_user = self.chatObject.text()
        time = datetime.now().strftime("%H:%M:%S")

        header = {
            'type': 'msg',
            'size': len(msg),
            'to': to_user,
            'from': from_user,
            'time': time
        }
        t = False
        if self.sendFileFlag and self.msgContainer.toPlainText() == "接收":
            header['type'] = 'getFile'
            self.sendFileFlag = False
            t = True

        header_json = json.dumps(header).encode('utf-8')
        header_json_len = len(header_json)
        print("发送： ", header_json_len)
        # 告诉服务器我的json数据有多大
        self.sock.send(struct.pack("i", header_json_len))
        # 告诉服务器我的json数据，里面包含了一些信息
        self.sock.send(header_json)
        # 告诉服务器我的msg数据
        self.sock.sendall(msg)

        # 发送方消息
        user_from = self.user + "   " + datetime.now().strftime("%H:%M:%S") + "\n"
        self.insertText(user_from, "#00aa00", 1)

        msg_from = self.msgContainer.toPlainText() + "\n\n"
        self.insertText(msg_from, "#000", align=1)

        # 让窗口焦点到最下面
        self.chatShow.moveCursor(QTextCursor.End)

        # 清空消息输入框
        self.msgContainer.setPlainText("")

        if t:
            self.clientGetFile(self.fileJson)
            t = False

        # 保存聊天记录
        self.saveChatRecord(self.user, self.chatObject.text())


    def addBtnClicked(self):
        add_user = self.searchOradd.text()
        if add_user == "":
            self.informationDialog("请输入对方账号进行添加")
            return
        res = self.addFriendDialog("是否添加 {} 为好友".format(add_user))
        if res:
            # 如果确认加好友就发送 数据
            to_user = add_user
            from_user = self.user
            time = datetime.now().strftime("%H:%M:%S")
            header = {
                'type': 'addFriend',
                'to': to_user,
                'from': from_user,
                'time': time
            }
            header_json = json.dumps(header).encode('utf-8')
            header_json_len = len(header_json)
            # 告诉服务器我的json数据有多大
            self.sock.send(struct.pack("i", header_json_len))
            # 告诉服务器我的json数据，里面包含了一些信息
            self.sock.send(header_json)

            # 清空输入框
            self.searchOradd.setText("")

    # 客户端时刻监控服务器传出来的数据
    def recvAll(self, conn):
        while True:
            print("开始从缓冲区读取此次json的长度")
            header_json_len = conn.recv(4)
            json_len = struct.unpack("i", header_json_len)[0]
            print("接受", json_len)
            print("开始读json")
            header_json = conn.recv(json_len)
            header_json = json.loads(header_json)
            print("读取的json", header_json)

            if header_json['type'] == "msg":
                self.handle_msg(header_json, conn)
            if header_json['type'] == 'addFriend':
                self.handle_addFriend(header_json, conn)
            if header_json['type'] == 'addFriendAgree':
                self.handle_friendAgree(header_json, conn)
            if header_json['type'] == 'file':
                self.handle_file(header_json, conn)
            if header_json['type'] == 'getFile':
                self.handle_getFile(header_json)


    # 处理别人发过来的消息
    def handle_msg(self, header_json, conn):
        to_user = header_json['to']
        msg_len = header_json['size']
        from_user = header_json['from']
        time = header_json['time']
        print("开始读取消息")
        msg = conn.recv(msg_len)
        print(msg)
        if to_user == self.user:
            data = msg.decode("utf-8")
            from_user = from_user + "   " + time + "\n"
            self.insertText(from_user, "#0000aa", align=0)
            msg_to = data + "\n\n"
            self.insertText(msg_to, "#000", align=0)
            # 让窗口焦点到最下面
            self.chatShow.moveCursor(QTextCursor.End)

            # 保存消息
            self.saveChatRecord(self.user, self.chatObject.text())

    # 处理添加好友申请
    def handle_addFriend(self, header_json, conn):
        to_user = header_json['to']
        from_user = header_json['from']
        print("收到添加好友,来自", from_user)
        if self.user == to_user:
            # 如果是该用户的好友请求，就解封好友申请区域
            self.from_user = from_user
            self.showFriendAdd()

    # 处理好友申请同意
    def handle_friendAgree(self, header_json, conn):
        to_user = header_json['to']
        from_user = header_json['from']
        print("收到好友申请同意,来自", from_user)
        if self.user == to_user:
            self.listWidget.addItem(from_user)
            # 保存新朋友到文件
            print(to_user, from_user, "**********")
            self.saveFriendList(to_user, from_user)
            print("已添加")

    # 处理文件发送
    def handle_file(self, header_json, conn):
        self.fileJson = header_json
        to_user = header_json['to']
        from_user = header_json['from']
        file = header_json['filePath'].split("/")[-1]
        time = header_json['time']
        if self.user == to_user:
            self.sendFileFlag = True
            self.insertText(from_user + "   " + time + "\n", "#0000aa", 0)
            self.insertText("「系统通知」：{}向您发送了{}文件，接受文件请回复'接收'\n\n".format(from_user, file), "#0000aa", 0)
            # 保存聊天记录
            self.saveChatRecord(self.user, self.chatObject.text())
            # 让窗口焦点到最下面
            self.chatShow.moveCursor(QTextCursor.End)

    # 处理接收文件
    def handle_getFile(self, header_json):
        to_user = header_json['to']
        from_user = header_json['from']
        fileName = self.fileJson['filePath']
        time = header_json['time']
        if self.user == to_user:
            self.insertText(from_user + "   " + time + "\n", "#00a", 0)
            self.insertText("「系统通知」：{}接收了您发送的文件{}\n\n".format(to_user, fileName.split("/")[-1]), "#00a", 0)

            self.saveChatRecord(self.user, self.chatObject.text())
            # 让窗口焦点到最下面
            self.chatShow.moveCursor(QTextCursor.End)

    def insertText(self, text, color, align):
        """
        插入msg到聊天框中
        :param text: 要插入的值
        :param color: 显示的颜色
        :param align: 显示的位置 0是左边，1是右边
        :return:
        """
        cursor = self.chatShow.textCursor()
        cursor.movePosition(QTextCursor.End)
        fmt = cursor.charFormat()
        fmt.setForeground(QColor(color))
        textBlockFormat = cursor.blockFormat()

        if align == 1:
            textBlockFormat.setAlignment(Qt.AlignRight)
        else:
            textBlockFormat.setAlignment(Qt.AlignLeft)
        cursor.mergeBlockFormat(textBlockFormat)
        cursor.insertText(text, fmt)

    # 添加好友弹窗
    def addFriendDialog(self, text):
        # 参考： https://www.cnblogs.com/leokale-zz/p/13106721.html
        res = QMessageBox.question(self.mainWindow, "询问", text, QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if res == QMessageBox.Yes:
            return True

    # 同意好友申请
    def agreeFriend(self):
        """
        同意好友申请，把这个好消息告诉申请人
        :return:
        """
        from_user = self.user

        # 发请求的人现在变成了接收方
        to_user = self.from_user

        # 保存新朋友到文件
        print(from_user, to_user, "######")
        self.saveFriendList(from_user,to_user)

        time = datetime.now().strftime("%H:%M:%S")
        header = {
            'type': 'addFriendAgree',
            'to': to_user,
            'from': from_user,
            'time': time
        }
        header_json = json.dumps(header).encode('utf-8')
        header_json_len = len(header_json)
        # 告诉服务器我的json数据有多大
        self.sock.send(struct.pack("i", header_json_len))
        # 告诉服务器我的json数据，里面包含了一些信息
        self.sock.send(header_json)

        # 把该好友显示到列表中
        self.listWidget.addItem(to_user)

        # 隐藏添加好友界面
        self.hideFriendAdd()

    # 显示好友申请界面，左下角
    def showFriendAdd(self):
        """
        解封好友添加界面
        :return:
        """
        self.widget_8.setVisible(True)
        self.add_friend_msg.setText("{}请求添加好友".format(self.from_user))
    # 隐藏好友申请界面
    def hideFriendAdd(self):
        """
        封印好友添加界面
        :return:
        """
        self.widget_8.setVisible(False)
        self.add_friend_msg.setText("")

    # 加载好友列表
    def loadFriendList(self):
        path = "assets/config/"
        try:
            with open(path + "friendList.json", "r") as file:
                info = json.load(file)
                friend_list = info[self.user]
                print(friend_list)
                for friend in friend_list:
                    self.listWidget.addItem(friend)
        except Exception as e:
            print(e)
            print("只是一个简单的文件不存在报错，问题不大，别慌...")
    # 保存好友列表到文件
    def saveFriendList(self, obj, friend):
        """
        将好友列表保存到文件中
        :param obj: 自己
        :param friend: 好友
        :return:
        """
        # 将该用户写入文件
        path = "assets/config/"
        info = {}
        # 先将数据读出来
        try:
            with open(path + "friendList.json", "r") as file:
                info = json.load(file)
        except Exception as e:
            print(e)
            print("只是一个简单的文件不存在报错，问题不大，别慌...")
        print("info1;  ", info)
        if len(info) == 0:
            info = {obj: [friend]}
            print("info2:  ", info)
        else:
            print(obj,'你好啊')
            if obj in info.keys():
                info[str(obj)].append(friend)
            else:
                info[str(obj)] = [friend]
        # 再将数据写进去
        print("las:  " ,info)
        try:
            with open(path + "friendList.json", "w") as file:
                json.dump(info, file)
        except Exception as e:
            print(e)
            print("只是一个简单的文件不存在报错，问题不大，别慌...")

    # 显示或隐藏emoji容器
    def displayEmojiContaniner(self):
        # 先将标志置反，代表接下来要显示的状态
        self.showEmojiFlag = not self.showEmojiFlag
        self.emoji_container.setVisible(self.showEmojiFlag)

    # 初始化多个槽与信号
    def initSlotSignal(self):
        # 建立槽与信号
        # 绑定listWidget点击函数
        self.listWidget.itemClicked.connect(self.listItemClicked)
        # 好友申请同意按钮
        self.agree_btn.clicked.connect(lambda: self.agreeFriend())
        # 绑定发送消息按钮函数
        self.sendMsg_btn.clicked.connect(self.sendMsgClicked)
        # 绑定添加好友按钮函数
        self.add_btn.clicked.connect(self.addBtnClicked)
        # 绑定点击表情按钮显示emoji容器
        self.send_emoji_btn.clicked.connect(self.displayEmojiContaniner)
        # 绑定所有的emoji点击事件
        self.emoji_1.clicked.connect(lambda :self.emojiClicked('😄'))
        self.emoji_2.clicked.connect(lambda :self.emojiClicked('😍'))
        self.emoji_3.clicked.connect(lambda :self.emojiClicked('😂'))
        self.emoji_4.clicked.connect(lambda :self.emojiClicked('😅'))
        self.emoji_5.clicked.connect(lambda :self.emojiClicked('🥺'))
        self.emoji_6.clicked.connect(lambda :self.emojiClicked('😘'))
        self.emoji_7.clicked.connect(lambda :self.emojiClicked('🙁'))
        self.emoji_8.clicked.connect(lambda :self.emojiClicked('😤'))
        self.emoji_9.clicked.connect(lambda :self.emojiClicked('😡'))
        self.emoji_10.clicked.connect(lambda :self.emojiClicked('🤔'))
        self.emoji_11.clicked.connect(lambda :self.emojiClicked('👍'))
        self.emoji_12.clicked.connect(lambda :self.emojiClicked('🐶'))
        self.send_file_btn.clicked.connect(self.sendFileClicked)


    # 初始化部分控件
    def initElements(self):
        # 取消macos 自带的部件晕圈效果（一个蓝色的边框）
        self.searchOradd.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.listWidget.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        # 设置添加联系人按钮
        self.add_btn.setIcon(QtGui.QIcon("assets/imgs/icon/add.svg"))
        # 设置同意拒绝按钮
        self.agree_btn.setIcon(QtGui.QIcon("assets/imgs/icon/agree.svg"))
        self.refuse_btn.setIcon(QtGui.QIcon("assets/imgs/icon/refuse.svg"))
        # 设置聊天输入框不可用
        self.msgContainer.setVisible(False)
        # 设置发送消息按钮不可用
        self.sendMsg_btn.setVisible(False)
        # 设置好友申请不显示
        self.hideFriendAdd()
        # 设置emoji_container不显示
        self.emoji_container.setVisible(False)

    # 发送表情按钮被单击
    def emojiClicked(self, data):
        # 将表情插入到输入框中
        self.msgContainer.insertPlainText(data)
        # 关闭emoji容器
        self.displayEmojiContaniner()

    # 保存聊天记录
    def saveChatRecord(self, from_user, to_user):
        """
        保存二人的聊天记录
        :param from_user: 客户端用户
        :param to_user: 聊天对象
        :return:
        """
        path = "assets/config/" + from_user + "to" + to_user + ".record"
        with open(path, 'w', encoding='utf-8') as file:
            file.write(self.chatShow.toHtml())
    # 加载聊天记录
    def loadChatRecord(self, from_user, to_user):
        """
        读取二人的聊天记录
        :param from_user: 客户端用户
        :param to_user: 聊天对象
        :return:
        """
        self.chatShow.setText("")
        path = "assets/config/" + from_user + "to" + to_user + ".record"
        try:
            with open(path,encoding='utf-8') as file:
                data = file.read()
                self.chatShow.setHtml(data)
                # 让窗口焦点到最下面
                self.chatShow.moveCursor(QTextCursor.End)
        except Exception as e:
            print(e)
            print("别慌，稳住...")

    # 发送文件按钮被单击
    def sendFileClicked(self):
        fileName = QFileDialog.getOpenFileName(self.mainWindow, "选取文件", os.getcwd(),"All Files(*.*)")

        to_user = self.chatObject.text()
        from_user = self.user
        time = datetime.now().strftime("%H:%M:%S")
        header = {
            'type': 'file',
            'to': to_user,
            'from': from_user,
            'filePath': fileName[0],
            'time': time
        }
        header_json = json.dumps(header).encode('utf-8')
        header_json_len = len(header_json)
        # 告诉服务器我的json数据有多大
        self.sock.send(struct.pack("i", header_json_len))
        # 告诉服务器我的json数据，里面包含了一些信息
        self.sock.send(header_json)

        self.insertText(self.user + "   " + time + "\n", "#0a0", 1)
        self.insertText("「系统通知」：您向{}发送了{}文件\n\n".format(to_user, fileName[0].split("/")[-1]), "#0a0", 1)

        self.saveChatRecord(self.user, self.chatObject.text())
        # 让窗口焦点到最下面
        self.chatShow.moveCursor(QTextCursor.End)
    def clientGetFile(self, header_json):
        to_user = header_json['to']
        from_user = header_json['from']
        fileName = header_json['filePath']
        print(fileName)
        time = header_json['time']
        self.insertText(self.user + "   " + time + "\n", "#0a0", 1)
        self.insertText("「系统通知」：您接收收了{}发送的文件{}\n\n".format(from_user, fileName.split("/")[-1]), "#0a0", 1)

        self.saveChatRecord(self.user, self.chatObject.text())
        # 让窗口焦点到最下面
        self.chatShow.moveCursor(QTextCursor.End)
        index = fileName.rindex("/")
        print(fileName[:index])
        os.system("open " + fileName[:index])
