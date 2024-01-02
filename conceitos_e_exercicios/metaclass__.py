"""
metaclass -> object ->classe -> objeto
parent class da class object

Seu objeto é um objeto da sua classe
Sua classe é um objeto da classe type (type é uma metaclass), sua classe herda todos os metódos e atributos de type
type('Name', (Bases,), __dict__)

a classe type() cria uma nova classe
clase = type(classname, herança(object), {}(seção dos atributos/metódos dos objetos da classe))

 __new__ da metaclass é chamado e cria a nova classe
 __call__ da metaclass é chamado com os argumentos e chama:
 __new__ da class com os argumentos (cria a instância)
 __init__ da class com os argumentos
 __call__ da metaclass termina a execução


Métodos importantes da metaclass
# __new__(metaclass, classname, herança(), dict(dos metódos e atributos dos objetos da classe)) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa o objeto, atribuindo seus metódos e atributos)


 "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê).

São especialmente uteis para dar maior personalização controle na criação de novas classes

"""

def my_repr(self): #Substitui metódo
    return f'{self.__class__.__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, classname, heranca, dict):    
        classe = super().__new__(mcs, classname, heranca, dict)
        classe.__repr__ = my_repr
        
        if ('Acelerar' not in classe.__dict__) or not callable(classe.__dict__['Acelerar']):
            raise NotImplementedError('Implemente o metódo Acelerar')

        return classe
    
    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs) #Incializa os atributos na metaclass type e atribui valores

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')

        return instancia
    
    
class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls) #Cria o objeto na parent class metaclassse
        return obj
    

    def __init__(self, nome) -> None:
        self.nome = nome

    def Acelerar(self):
        print('Acelerando')

p1 = Pessoa('Carlão')
print(p1)