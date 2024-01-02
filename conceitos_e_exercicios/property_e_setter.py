"""
@property
Faz com que um metódo se comporte como um atributo

@atributo.setter
permite que o valor de um atributo property seja alterado


Todos atributos estão no escopo da classe e por isso não há a necessidade de indicar global, ou retornar atributos, para confirmação sua criação ou alteração
"""
from random import randint, uniform
chaves = ['marca', 'comprimento','expessura', 'cor']

class Caneta:
    def __init__(self, marca:str,comprimento:float, cor:str, expessura:float) -> None:
        self.__marca = marca
        self.__comprimento = comprimento
        self.__expessura = expessura
        self.__cor = cor 
        

    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def comprimento(self):
        return self.__comprimento
    
    @property
    def expessura(self):
        return self.__expessura
    
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, valor):
        self.__cor = valor

def listar(obj):
    global chaves
    iterator = iter(chaves)
    atributos = {next(iterator).capitalize(): valor for valor in vars(obj).values()}
    for chave, valor in atributos.items():
        print(f'{chave}: {valor}')


def gera_obj(objattr, marca:str):
    global chaves
    iterator = iter(chaves)
    items = vars(objattr).items()

    temp = Caneta(**{next(iterator): valor if [valor] != [dupla[-1] for pos, dupla in enumerate(items) if pos == 0] else marca for chave, valor in items})
    return temp

bic = Caneta('Bic',12, 'Azul', 2)
listar(bic)
print('')

fab = gera_obj(bic, 'Faber')
fab.cor = 'Amarela'
listar(fab)
print('')
nes = gera_obj(bic, 'Nestle')
nes.cor = 'Roxa'
listar(nes)