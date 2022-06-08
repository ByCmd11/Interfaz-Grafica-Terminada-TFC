from PySide2.QtWidgets import QWidget
from views.login import LoginForm


class LoginWindow(QWidget, LoginForm):

    def __init__(self):
        super().__init__()
        # desplegamos la interfaz grafica
        self.setupUi(self)
        # al pulsar el boton nos unimos al chat
        self.joinButton.clicked.connect(self.unirseChat)

    def unirseChat(self):
        usuario = self.usernameLineEdit.text()
        # si el usuario no esta vacio mosyramos la ventana del chat
        if usuario != '':
            from controllers.chat import ChatWindow
            self.chat_window = ChatWindow(usuario)
            self.chat_window.show()
            self.close()
