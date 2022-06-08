from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt

from views.chat import ChatForm
from controllers.login import LoginWindow

import socket
import threading


class ChatWindow(QWidget, ChatForm):

    def __init__(self, username):
        super().__init__()

        self.username = username
        self.setupUi(self)

        self.connect()

        self.sendButton.clicked.connect(self.enviarMensajes)

    def connect(self):
        datos = ('127.0.0.1', 55555)
        af_inet = socket.AF_INET
        sock_stream = socket.SOCK_STREAM

        self.client = socket.socket(af_inet, sock_stream)
        self.client.connect(datos)

        receive_thread = threading.Thread(target=self.recivirMensajes)
        receive_thread.daemon = True
        receive_thread.start()
        self.label.setText(f"{self.username}")
        self.client.send(self.username.encode('utf-8'))

    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.client.close()
        self.close()

    def recivirMensajes(self):
        while True:
            try:
                # recivimos los mensajes
                mensaje = self.client.recv(1024).decode('utf-8')
                # añadimos los mensajes recividos al cuadro de texto
                self.chatTextEdit.append(mensaje)
                # alinemaos los mensajes recividos a la izquirda
                self.chatTextEdit.setAlignment(Qt.AlignLeft)
            except:
                self.client.close()
                break

    def enviarMensajes(self):
        # cogemos los mensajes escritos en el cuadro de texto
        mensaje = self.messageLineEdit.text()
        # añadimos nustro normbre al mensaje
        mensaje = f"{self.username}: {mensaje}"
        # enviamos el mensaje
        self.client.send(mensaje.encode('utf-8'))
        # añadimos los mensajes escritos al cuadro de texto
        self.chatTextEdit.append(mensaje)
        # alienamos los mensajes enviaddos a las derecha
        self.chatTextEdit.setAlignment(Qt.AlignRight)
        # limpaimos el cudro donde se envian los mensajes
        self.messageLineEdit.clear()
