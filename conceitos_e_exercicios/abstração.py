"""
Abstração é um conceito o qual, uma classe, metódo ou atributos não podem ser instaciados diretamente pela parent class, para se ter acesso aos metodos e atributos dessa classe abstrata é preciso iplementar os metódos e atributos abstratos dessa classe abstrata em uma child class

Abstração é essencial para definir o contrato/assinatura dos metódos de uma classe e de suas childs class, e o corpo dos metódos(forma como é utilizado/passado) pode ser diferente nas childs class

--------------------------------------------------------
Polimorfismo um mesmo metódo pode se comportar de formas diferentes nas childs class, mesmo havendo uma mesma assinatura/contrato.
"""
from os import system
from pathlib import Path
#Pegou caminho absoluto do módulo atual, e concatenou com 'Log.txt'
LogFile = Path(__file__).parent / 'Log.txt'

class Log:
    #Se alguém tentar instanciar um objeto na classe log, e usar o metódo de obj login, vai retornar o erro NotImplementeErrror
    def _Login(self, msg):
        raise NotImplementedError('Não instancie essa classe diretamente, implemente o metódo login em uma child class')
    #O metódo __login vai ser executado na child class, passando 'ERROR: {msg}' como argumento para o metódo __Login da child class
    def LoginError(self, msg):
        return self._Login(f'ERROR: {msg}')

    def LoginSucess(self, msg):
        return self._Login(f'SUCESS: {msg}')
    
#Os objetos instanciados na child class(LogFileMixen) vão poder usar o metódo Login
class LogFileMixin(Log):
        def _Login(self, msg):
            print(f'Salvando mensagem no arquivo Log.txt')
            mensagem = f'{msg}.|{self.__class__.__name__}'
            with open(LogFile, 'a', encoding='utf8') as PathLog:
                PathLog.write(mensagem)

class LogPrintMixin(Log):
    def _Login(self, msg):
        print(f'{msg}.|{self.__class__.__name__}')


key = LogPrintMixin()

key.LoginError('Senha invalida')
key.LoginSucess('Entrou com sucesso na conta')

key2 = LogFileMixin()
key2.LoginSucess('Logou com sucesso na conta')
key2.LoginError('Senha Incorreta')


class Eletronicos:
    def __init__(self, nome) -> None:
        self.nome = nome 
        self._ligado = False
    
    def ligar(self):
        if not self._ligado:
            self._ligado = True
    
    def desligar(self):
        if self._ligado:
            self._ligado = False
system('clear')
class Smartphones(Eletronicos, LogPrintMixin):
    def __init__(self, nome) -> None:
          super().__init__(nome)
    #Implemente o metódo ligar na child class smartphone
    def ligar(self):
        if not self._ligado:
            super().ligar()
            msg = f'O smartphone {self.nome} está ligado'
            self.LoginSucess(msg)
        else:
            msg = f'O smartphone {self.nome} já estava ligado'
            self.LoginError(msg)
        
    
    def desligar(self):
        

        if not self._ligado:
            msg = f'O smartphone {self.nome} já estava desligado'
            self.LoginError(msg)
        else:
            super().desligar()
            msg = f'O smartphone {self.nome} foi desligado'
            self.LoginSucess(msg)

        
apple = Smartphones('Iphone')
sansung = Smartphones('Galaxy')

apple.ligar()
apple.ligar()
apple.desligar()
apple.ligar()
apple.desligar()
apple.desligar()
print('')
print('')
sansung.ligar()
sansung.desligar()
sansung.desligar()
sansung.ligar()
sansung.ligar()