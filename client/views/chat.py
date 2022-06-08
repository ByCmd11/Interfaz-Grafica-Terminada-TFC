# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'chat.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ChatForm(object):
    def setupUi(self, chatForm):
        if not chatForm.objectName():
            chatForm.setObjectName(u"chatForm")
        chatForm.resize(656, 871)
        self.frame = QFrame(chatForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 661, 91))
        self.frame.setStyleSheet(u"background-color: rgb(80, 44, 142);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 101, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        font3 = QFont()
        font3.setFamily("Arial")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(760, 60, 61, 16))
        self.label_2.setStyleSheet(u"color: white;")
        self.chatTextEdit = QTextEdit(chatForm)
        self.chatTextEdit.setObjectName(u"chatTextEdit")
        self.chatTextEdit.setGeometry(QRect(0, 90, 661, 711))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chatTextEdit.setFont(font)
        self.chatTextEdit.setStyleSheet("background-color: rgb(23, 24, 37);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "\n"
                                        "")
        self.chatTextEdit.setReadOnly(True)
        self.frame_2 = QFrame(chatForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 780, 661, 91))
        self.frame_2.setStyleSheet("background-color: rgb(80, 44, 142);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.messageLineEdit = QLineEdit(self.frame_2)
        self.messageLineEdit.setObjectName(u"messageLineEdit")
        self.messageLineEdit.setGeometry(QRect(10, 10, 501, 61))
        self.messageLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(133, 131, 131);")
        font1 = QFont()
        font1.setPointSize(10)
        self.messageLineEdit.setFont(font1)
        self.sendButton = QPushButton(self.frame_2)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(530, 30, 93, 28))
        self.sendButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendButton.setStyleSheet("background-color: rgb(133, 131, 131);")
        icon1 = QIcon()
        icon1.addFile(u"client/assets/paper-plane-icon-614x460.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.sendButton.setIcon(icon1)
        self.sendButton.setIconSize(QSize(120, 110))
        self.sendButton.setFlat(True)

        self.retranslateUi(chatForm)

        QMetaObject.connectSlotsByName(chatForm)
    # setupUi

    def retranslateUi(self, chatForm):
        chatForm.setWindowTitle(
            QCoreApplication.translate("chatForm", u"Form", None))
        self.label.setText("")

        self.label_2.setText(QCoreApplication.translate(
            "chatForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">LOGOUT</span></p></body></html>", None))
        self.messageLineEdit.setPlaceholderText(
            QCoreApplication.translate("chatForm", u"Escribe...", None))
        self.sendButton.setText("")
    # retranslateUi
