"""
class/obj.__class__ / type(class/obj) - Retorna a parent class, ou classe que o objeto é instância

obj.__class__.__name__ -> Retorna o nome da classe

class.__base__ -> Retorna a parent class de uma classe

class.__bases__ -> Retorna todas as parents class que uma classe herda diretamente

class.__subclasscheck__(classe) -> Checa se uma classe é um subclasse de class

class.__subclasses__() -> Retorna uma lista com as childs class, que herdam diretamente da parent class, class


instancia/objeto != subclasse



"""

class ParentClass:
    ...

class ChildClass(ParentClass):
    ...

class GrandSonClass(ChildClass):
    ...

print(GrandSonClass.__base__)
print(GrandSonClass.__bases__)
print(ParentClass.__subclasses__())