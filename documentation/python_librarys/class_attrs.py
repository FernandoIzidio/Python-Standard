"""
todo metódo por padrão é um metódo de objeto(exceto o metódo __new__() - Que sera sempre um metódo de classe para gerar novas instãncias, ou gerar novas classes, ou seja o __new__() - só tera acesso a classe no seu escopo, e ao gerar uma instância da classe, passara a ter acesso aos objetos)

class/obj.__class__ / type(class/obj) - Retorna a parent class, ou classe que o objeto é instância

obj.__class__.__name__ -> Retorna o nome da classe

class.__base__ -> Retorna a parent class de uma classe

class.__bases__ -> Retorna todas as parents class que uma classe herda diretamente

class.__subclasscheck__(classe) -> Checa se uma classe é um subclasse de classe

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