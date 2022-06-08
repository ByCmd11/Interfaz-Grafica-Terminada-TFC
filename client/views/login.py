# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'login.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class LoginForm(object):
    def setupUi(self, loginForm):
        if not loginForm.objectName():
            loginForm.setObjectName(u"loginForm")
        loginForm.resize(412, 484)
        self.frame = QFrame(loginForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 421, 491))
        self.frame.setStyleSheet(u"background-color: rgb(23, 24, 37);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-11, -1, 451, 71))

        self.label.setStyleSheet(u"background-color: rgb(80, 44, 142);\n"
                                 "border-radius: 5px;")
        self.label_2 = QLabel(loginForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 190, 171, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.usernameLineEdit = QLineEdit(loginForm)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(80, 220, 261, 31))
        self.usernameLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(133, 131, 131);")
        self.joinButton = QPushButton(loginForm)
        self.joinButton.setObjectName(u"joinButton")

        self.joinButton.setGeometry(QRect(80, 280, 131, 41))
        self.joinButton.setStyleSheet("background-color: rgb(80, 44, 142);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius: 20%;")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.joinButton.setFont(font)

        self.retranslateUi(loginForm)

        QMetaObject.connectSlotsByName(loginForm)
    # setupUi

    def retranslateUi(self, loginForm):
        loginForm.setWindowTitle(
            QCoreApplication.translate("loginForm", u"Form", None))
        self.label.setText(QCoreApplication.translate(
            "loginForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color: white; font-weight:600;\">Chat entre pares</span></p></body></html>", None))
        self.usernameLineEdit.setPlaceholderText(
            QCoreApplication.translate("loginForm", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate(
            "loginForm", u"Introduza Usuario", None))
        self.joinButton.setText(
            QCoreApplication.translate("loginForm", u"Unete", None))
    # retranslateUi
