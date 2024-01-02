"""
Classes que modificam/substituem o comportamento de outras classes/metódos/funções
-__init__ 
- Metódo init recebe o objeto temporário(invisivel) e recebe a função
- Vai transformar a função/metódo/ classe decorada em um objeto
- Esse objeto vai ser chamado e ter seus argumentos para call

__call__
- Recebe o objeto temporário executado(função)e os argumentos da função


quando a class decorator é chamada antes do python, o init recebe os atributos do objeto e retorna o objeto que posteriormente é executado, e o objeto recebe a função e os argumentos, ou seja quando a class decorator é executada antes:
O __init__ recebe os atributos do objeto
O __call__ recebe a função
a função interna de call recebe os argumentos da função
"""
from os import system
from typing import Any
from time import sleep

class Decorator_Class:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any: #Modificação da função abaixo
        if all(isinstance(argumento, (int, float)) for argumento in args) and all(isinstance(argumento, (int, float)) for argumento in kwds.values()):
            return self.func(*args, **kwds) #Retorna a execução função antiga após fazer a modificação. 
        raise TypeError
    
class Replace_Function:
    def __init__(self) -> None:...
    
    def __call__(self, func) -> Any:            
        def interna(*args, **kwargs):
            return 'Função substituida!!!'
        return interna
                         
#Decorator_Class(objtemp(invisivel), Multiplicar) 
#Um objeto será retornado após isso, e esse objeto sera executado
@Decorator_Class
def Multiplicar(x, y): #Equivale ao objeto executado
    return x*y

@Replace_Function()
def Dividir(x, y):
    return x/y

print(Dividir(8, 4))
input()

while True:
    try:
        system('clear')
        #Multiplicar('', 7)
        print(Multiplicar(int(input('Digite um número:')), float(input('Digite outro número: '))))
        while True:
            opt = input('Deseja continuar[S/N]: ').upper()
            if opt in ('S', 'N'):
                break
            system('clear')
            print('ERRO: Digite uma opção válida')
            sleep(1)
        if opt == 'N':
            break
    except (TypeError, ValueError):
        print('ERRO: Forneça apenas números como argumento para a função')
        sleep(1)

