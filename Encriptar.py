from cryptography.fernet import Fernet




class Encriptar:
    global llave 
    llave = Fernet.generate_key()
    global cifrador 
    cifrador = Fernet(llave)
    
    def encriptarMensaje(mensaje):

        mensaje_encriptado = cifrador.encrypt(bytes(mensaje.encode("utf-8")))
        return mensaje_encriptado
    
    def desencriptarMensaje(mensaje):
        mensaje_desencriptado_bytes = cifrador.decrypt(mensaje).decode("utf-8")
        
        return mensaje_desencriptado_bytes


