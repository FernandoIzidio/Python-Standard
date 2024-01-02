
"""
todo decorator tem quer retornar o objeto que modifica, ou substitui-lo:
Metódos para criar o decorator:
    __new__ primeiro metódo usado para criar objeto, o objeto da class decorator passa a se comportar como o obojeto a ser modificado. new deve retornar o objeto

    __call__ recebe argumentos do objeto, deve retornar o objeto que modifica, ou substitui-lo

Quando chamado antes da hora o __call__ recebe a func, e uma função interna recebe os argumentos da func
    """

from typing import Any


class DecoratorClass:
    def __new__(cls, function):
        objeto   = super().__new__(cls)
        objeto.func= function
        return objeto

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print('Fala OI!!!!')
        return self.func(*args, **kwds)

@DecoratorClass
def multi(x, y):
    return x * y


print(multi(8,6))
print(multi(7,5))

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
            return function(*args, **kwargs) 
        return interna

@DecoratorClass2('truco', 'LADRÃO')
def divide(x, y):
    return x / y

print(divide(8, 2))
print(divide(9, 2))
print(divide(16,2 ))
print(divide(43, 2))