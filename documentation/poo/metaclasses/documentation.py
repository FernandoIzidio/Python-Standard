
"""
Toda classe em python herda todos os metódos e atributos da metaclasse object 

Metaclasses são as responsáveis por criar outras classes
É util quando se quer personalizar a forma de criação de uma classe

classe = type(classname, herança, atributosdaclasse) - type retorna a classe de um objeto, ou cria uma nova classe

Toda metaclasse herda de type

Metaclass é uma classe que criar outras classes

__new__ - Só tem acesso a classe, ou seja mcs vai referênciar a própria classe.

mcs é uma convenção para metaclasse, assim com self para metódos de objetos, e cls para metódos de classe

metódos de metaclasses:
    __new__(mcs, classname, herança, atributosclasse) - Responsável por tratar da criação da classe, deve retornar a classe

    __call__(cls, *args, **kwargs) - Torna e classe callable, Responsável pela criação de instancias da classe, deve retornar um objeto da classe

__new__ de uma classe normal vai chamar o __call__ de uma metaclasse, para receber as instâncias, ou objeto da classe

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
