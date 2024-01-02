"""
Polimorfimos:
Principio que permite que subclasses derivadas de uma mesma parent class, tenha metódos de mesmas assinatura/contrato, mas comportamentos/formas diferentes

Contrato/Assinatura do metódo: Nome, nome dos parametros, quantidade de parametros, retornos iguais

List copy Substituion principle:
-Um objeto de uma parent class, deve ser substituido por objetos da child class sem quebrar a aplicação
-- Para isso é preciso que os metódos de uma parent class, tenham a mesma assinatura nas childs class



======

python não suporta sobrecarga de metódos(overload)
python suporta sobreposição de metódos(override)
"""
from abc import abstractclassmethod, ABC

class Notificao(ABC):
    def __init__(self, mensagem) -> None:
        super().__init__()
        self.mensagem = mensagem

    @abstractclassmethod
    def enviar(self) -> bool:...


class SMS(Notificao):
    def __init__(self, mensagem) -> None:
        super().__init__(mensagem)

    def enviar(self) -> bool:
        print(f'{self.mensagem}\nMensagem enviada com sucesso por SMS.')
        return True

class Whatsapp(Notificao):
    def enviar(self) -> bool:
        print(f'{self.mensagem}\nMensagem enviada com sucesso por Whatsapp')
        return True


#Metódo de mesma assinatura se comporta de maneiras diferentes, dependendo da child class
def notificar(objeto: Notificao) -> None:
    checknotification = objeto.enviar()

    if checknotification:
        print('Notificação enviada')
    else:
        print('Notificação não enviada')
msg1 = SMS('Flamengo é piada')
msg2 = Whatsapp('Flamengo é chacota')
notificar(msg1)
print('')
notificar(msg2)

