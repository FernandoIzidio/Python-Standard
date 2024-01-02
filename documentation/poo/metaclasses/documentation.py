
"""
Toda classe em python herda todos os metódos e atributos da metaclasse object ou da metaclasse parent,

Metaclasses são as responsáveis por criar outras classes
É util quando se quer personalizar a forma de criação de uma classe

classe = type(classname, herança, atributosdaclasse) - type retorna a classe de um objeto, ou cria uma nova classe

metódos de metaclasses:
    __new__(mcs, classname, herança, atributosclasse) - Responsável por tratar da criação da classe, deve retornar a classe

    __call__(cls, *args, **kwargs) - Responsável pela criação de instancias da classe, deve retornar um objeto da classe

class(metaclass=) - Defina a metaclasse de uma classe

toda metaclasse tem quer herdar da metaclasse type
metaclasse(type)
"""

from typing import Any


class MetaClasse(type):

    def __new__(mcs, classname, bases, classattrs):
        classe = super().__new__(mcs,classname, bases, classattrs)
        classe.passwd = 6835
        return classe
    

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        objetoofclass = super().__call__(*args, **kwds)

        if not hasattr(objetoofclass, 'abstrato') or not callable(getattr(objetoofclass, 'abstrato')):
            raise NotImplementedError('Implemente o metódo abstrato(self, ...)')
        
        return objetoofclass

class Myclass(metaclass=MetaClasse):
    def __init__(self, valor) -> None:
        self.attr1 = valor
        
    def abstrato(self):...
    


obj = Myclass(65)
print(obj.attr1)
print(obj.passwd)
