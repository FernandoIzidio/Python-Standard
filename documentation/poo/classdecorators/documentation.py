
"""
todo decorator tem quer retornar o objeto que modifica, ou substitui-lo:
Metódos para criar o decorator:
    __new__  metódo usado para criar objeto, o objeto da class decorator passa a se comportar como o objeto a ser modificado. new deve retornar o objeto

    __call__ recebe argumentos do objeto, deve retornar o objeto que modifica, ou substitui-lo

Quando chamado antes da hora o __call__ recebe a func, e uma função interna recebe os argumentos da func
Decorators @ são chamados apenas uma vez, exemplo @object object2 -> object(object2)

    """

from typing import Any


class DecoratorClass:
    def __new__(cls, function):
        objeto   = super().__new__(cls)
        objeto.func= function
        return objeto

    def __call__(self, message, *args: Any, **kwds: Any) -> Any:
        print('Fala OI!!!!')
        print(message)
        return self.func(*args, **kwds)

@DecoratorClass #Criando uma instância da classe Decorator Class passando como argumento de init uma função, todo vez que essa função for chamada, um objeto vai ser chamado, por isso o callable
def multi(x, y):
    return x * y


print(multi("OLÁAAA",8,6))
print(multi("Flamengo é piada",7,5))

class DecoratorClass2:
    def __new__(cls, *args):
        objeto = super().__new__(cls)
        return objeto

    def __init__(self, *args):
        self.argumentos = args

    def __call__(self, function) -> Any:
        def interna(*args, **kwargs):
            print(f'Função Moficada por {type(self)}')
            print('Argumentos de criação: ')
            print(*self.argumentos, sep='\n')
            return function(*args, **kwargs) #Executando comportamento padrão da função recebida
        return interna #Toda vez que o objeto for chamado 

@DecoratorClass2('truco', 'LADRÃO') #Criando instância da classe Decorator class2, e depois chamando esse objeto passando uma função como argumento do objeto, o objeto por sua vez retornara uma função modificada
def divide(x, y):
    return x / y

print(divide(8, 2))
print(divide(9, 2))
print(divide(16,2 ))
print(divide(43, 2))