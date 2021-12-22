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
        MainWindow.resize(643, 485)
        MainWindow.setStyleSheet("#widget_2{\n"
"    background-color: #F1F1F1;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(100, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("#widget_3,#widget_4,#widget_5{\n"
"    border-bottom: 1.5px solid #DCDCDC;\n"
"    background-color: #F1F1F1;\n"
"}")
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
        self.titleName = QtWidgets.QLabel(self.widget_3)
        self.titleName.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.titleName.setFont(font)
        self.titleName.setText("")
        self.titleName.setObjectName("titleName")
        self.vboxlayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.vboxlayout.addWidget(self.widget_4)
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 32))
        self.widget_6.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color:#F1F1F1;\n"
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
        self.widget_5.setObjectName("widget_5")
        self.vboxlayout.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

