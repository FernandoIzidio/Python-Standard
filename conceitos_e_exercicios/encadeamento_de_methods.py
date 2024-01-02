"""
Para fazer encadeamento de metódos, o metódo tem que retornar o próprio objeto

obj.metodo().metodo().metodo()

class Classe:
    def metodo(self):
        ...
        return self


"""

class Wireless:
    def set_user(self):
        print('Usuário Definido')
        return self

    def connect(self):
        print('Conectando')
        return self

    def desconect(self):
        print('Desconectado')
        return self


wifi = Wireless()
wifi.set_user().connect().desconect().set_user()