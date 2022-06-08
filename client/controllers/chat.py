from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt

from views.chat import ChatForm
from controllers.login import LoginWindow

import socket
import threading


class ChatWindow(QWidget, ChatForm):

    def __init__(self, usuario):
        #lLAMA AL CONSTRUCTOR DE LA CLASE QWidget
        super().__init__()
        
    #definimos el usuario
        self.usuario = usuario
    #Iniciamos la ventana
        self.setupUi(self)
        #Nos conectamos al servidor
        self.servidor()
        #Al pulsar el boton se envian los mensajes
        self.sendButton.clicked.connect(self.enviarMensajes)

    def servidor(self):
        datos = ('127.0.0.1', 55555)

    #Definimos el socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Nos conectamos a la dirreccion de la variable datps
        self.client.connect(datos)
    #Creamos un hilo para recivir los mensajes
        receive_thread = threading.Thread(target=self.recivirMensajes)
    #Iniciamos el hilo
        receive_thread.daemon = True
        receive_thread.start()
    #Ponemos el nombre de usuario en el cuadro de texto
        self.label.setText(f"{self.usuario}")

    #Enviamos el nombre de usaurio
        self.client.send(self.usuario.encode('utf-8'))


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
        mensaje = f"{self.usuario}: {mensaje}"
        # enviamos el mensaje
        self.client.send(mensaje.encode('utf-8'))
        # añadimos los mensajes escritos al cuadro de texto
        self.chatTextEdit.append(mensaje)
        # alienamos los mensajes enviaddos a las derecha
        self.chatTextEdit.setAlignment(Qt.AlignRight)
        # limpaimos el cudro donde se envian los mensajes
        self.messageLineEdit.clear()
