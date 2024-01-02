"""
Propertys Abstratos: 

@property
@abstractmethod
def atributo(...):...

Ao criar uma property abstrata na parent class, essa property e seu setter precisam ser implementados na child class
-a implementação da property pode ser por sobreposição
-A implementação da property também pode ser pela criação de um atributo de classe na child class

Seters abstratos: 

@atributo.setter
@abstractmethod
def atributo(...):...

@Parentclass.atributo.setter
def atributo(...)...

Ao criar um setter abstrato na parent class, ao implementar esse setter na child class, o namespace da parent class precisa estar na implementação desse setter


"""
from abc import ABC, abstractclassmethod

class AbstractPropertyPessoa(ABC):
    def __init__(self, name) -> None:
        super().__init__()
        self._name = name

    @property
    @abstractclassmethod
    def name(self):...



class AbstractSetterPessoa(ABC):
    def __init__(self, nome) -> None:
        super().__init__()
        self._nome = None
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    @abstractclassmethod
    def nome(self):...
        


class Pessoa(AbstractPropertyPessoa):
    def __init__(self, name) -> None:
        super().__init__(name)

    @property
    def name(self):
        return self._name


class Pessoa2(AbstractSetterPessoa):
    def __init__(self, nome) -> None:
        super().__init__(nome)
    
    @AbstractSetterPessoa.nome.setter
    def nome(self, valor):
        self._nome = valor


p1 = Pessoa('Carlão')
p2 = Pessoa2('Pedrão')
print(p2.nome)
print(p1.name)
p2.nome = 'Jorjão'
print(p2.nome)
