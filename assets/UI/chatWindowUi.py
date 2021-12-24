# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 483)
        MainWindow.setStyleSheet("#widget_2{\n"
"    border-left: 12px;\n"
"    background-color: #fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(130, 16777215))
        self.widget.setStyleSheet("#widget_7{\n"
"    background-color: #F7F7F7;\n"
"}\n"
"#listWidget{\n"
"    border: none;\n"
"    background-color:#F7F7F7;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_7.setStyleSheet("#searchOradd{\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"    background-color:#ECECEC;\n"
"}")
        self.widget_7.setObjectName("widget_7")
        self.searchOradd = QtWidgets.QLineEdit(self.widget_7)
        self.searchOradd.setGeometry(QtCore.QRect(7, 10, 95, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchOradd.setFont(font)
        self.searchOradd.setStyleSheet("    background-color:#ECECEC;")
        self.searchOradd.setObjectName("searchOradd")
        self.add_btn = QtWidgets.QPushButton(self.widget_7)
        self.add_btn.setGeometry(QtCore.QRect(107, 10, 20, 21))
        self.add_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.add_btn.setMaximumSize(QtCore.QSize(31, 31))
        self.add_btn.setText("")
        self.add_btn.setIconSize(QtCore.QSize(16, 16))
        self.add_btn.setAutoDefault(False)
        self.add_btn.setDefault(False)
        self.add_btn.setFlat(False)
        self.add_btn.setObjectName("add_btn")
        self.verticalLayout.addWidget(self.widget_7)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.widget_3.setFont(font)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.chatObject = QtWidgets.QLabel(self.widget_3)
        self.chatObject.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chatObject.setFont(font)
        self.chatObject.setText("")
        self.chatObject.setObjectName("chatObject")
        self.vboxlayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setItalic(False)
        self.widget_4.setFont(font)
        self.widget_4.setObjectName("widget_4")
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setGeometry(QtCore.QRect(180, 130, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.widget_4)
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 32))
        self.widget_6.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color:#fff;\n"
"}")
        self.widget_6.setObjectName("widget_6")
        self.send_emoji_btn = QtWidgets.QPushButton(self.widget_6)
        self.send_emoji_btn.setGeometry(QtCore.QRect(10, 0, 30, 30))
        self.send_emoji_btn.setAutoFillBackground(False)
        self.send_emoji_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imgs/icon/smile.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_emoji_btn.setIcon(icon)
        self.send_emoji_btn.setIconSize(QtCore.QSize(23, 23))
        self.send_emoji_btn.setObjectName("send_emoji_btn")
        self.send_file_btn = QtWidgets.QPushButton(self.widget_6)
        self.send_file_btn.setGeometry(QtCore.QRect(44, 0, 30, 30))
        self.send_file_btn.setAutoFillBackground(False)
        self.send_file_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imgs/icon/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_file_btn.setIcon(icon1)
        self.send_file_btn.setIconSize(QtCore.QSize(23, 23))
        self.send_file_btn.setObjectName("send_file_btn")
        self.look_history_btn = QtWidgets.QPushButton(self.widget_6)
        self.look_history_btn.setGeometry(QtCore.QRect(80, 0, 30, 30))
        self.look_history_btn.setAutoFillBackground(False)
        self.look_history_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imgs/icon/history.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.look_history_btn.setIcon(icon2)
        self.look_history_btn.setIconSize(QtCore.QSize(23, 23))
        self.look_history_btn.setObjectName("look_history_btn")
        self.vboxlayout.addWidget(self.widget_6)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 125))
        self.widget_5.setStyleSheet("#msgContainer{\n"
"    border: none;\n"
"}")
        self.widget_5.setObjectName("widget_5")
        self.msgContainer = QtWidgets.QTextEdit(self.widget_5)
        self.msgContainer.setEnabled(True)
        self.msgContainer.setGeometry(QtCore.QRect(0, 0, 518, 125))
        self.msgContainer.setObjectName("msgContainer")
        self.sendMsg_btn = QtWidgets.QPushButton(self.widget_5)
        self.sendMsg_btn.setGeometry(QtCore.QRect(430, 90, 70, 32))
        self.sendMsg_btn.setObjectName("sendMsg_btn")
        self.vboxlayout.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "聊天"))
        self.searchOradd.setPlaceholderText(_translate("MainWindow", "搜索/添加"))
        self.label.setText(_translate("MainWindow", "Python For Chat"))
        self.sendMsg_btn.setText(_translate("MainWindow", "发送"))

