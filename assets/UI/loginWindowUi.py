# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(361, 272)
        MainWindow.setMinimumSize(QtCore.QSize(361, 230))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(64, 170, 251, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.savePassword = QtWidgets.QCheckBox(self.layoutWidget)
        self.savePassword.setObjectName("savePassword")
        self.horizontalLayout_3.addWidget(self.savePassword)
        self.autoLogin = QtWidgets.QCheckBox(self.layoutWidget)
        self.autoLogin.setObjectName("autoLogin")
        self.horizontalLayout_3.addWidget(self.autoLogin)
        self.retrievePassword = QtWidgets.QLabel(self.layoutWidget)
        self.retrievePassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retrievePassword.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.retrievePassword.setObjectName("retrievePassword")
        self.horizontalLayout_3.addWidget(self.retrievePassword)
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(70, 210, 220, 51))
        self.loginBtn.setAutoFillBackground(False)
        self.loginBtn.setObjectName("loginBtn")
        self.registerAccount = QtWidgets.QLabel(self.centralwidget)
        self.registerAccount.setGeometry(QtCore.QRect(10, 250, 60, 16))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.registerAccount.setFont(font)
        self.registerAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerAccount.setObjectName("registerAccount")
        self.topImage = QtWidgets.QLabel(self.centralwidget)
        self.topImage.setGeometry(QtCore.QRect(0, 0, 361, 91))
        self.topImage.setText("")
        self.topImage.setPixmap(QtGui.QPixmap("../imgs/topImage.jpg"))
        self.topImage.setScaledContents(True)
        self.topImage.setObjectName("topImage")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 100, 231, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.loginUser = QtWidgets.QLineEdit(self.layoutWidget1)
        self.loginUser.setEnabled(True)
        self.loginUser.setObjectName("loginUser")
        self.horizontalLayout.addWidget(self.loginUser)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 140, 231, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.loginPsd = QtWidgets.QLineEdit(self.layoutWidget2)
        self.loginPsd.setObjectName("loginPsd")
        self.horizontalLayout_2.addWidget(self.loginPsd)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登陆"))
        self.savePassword.setText(_translate("MainWindow", "记住密码"))
        self.autoLogin.setText(_translate("MainWindow", "自动登陆"))
        self.retrievePassword.setText(_translate("MainWindow", "找回密码"))
        self.loginBtn.setText(_translate("MainWindow", "登陆"))
        self.registerAccount.setText(_translate("MainWindow", "注册账号"))
        self.label.setText(_translate("MainWindow", "账号:"))
        self.label_2.setText(_translate("MainWindow", "密码:"))

