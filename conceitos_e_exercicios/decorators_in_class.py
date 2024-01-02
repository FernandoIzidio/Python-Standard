"""
decorators in class's

"""

#Esse decorator vai emular como se eu tivesse dentro da classe
def Repr_Decorator(cls): #Recebe classe
    #Crian o metódo repr modificado como se estivesse dentro da classe
    def personal_repr(self): #Cria metódo de objetos personal_repr
        return f'{self.__class__.__name__}({self.__dict__})'
    cls.__repr__ = personal_repr #Modificando/Trocando o repr da função pelo repr modificado
    return cls #Retornando a classe modificada com repr personalizado implementado


"""
class MyRepr:
    def __repr__(self) -> str:
        return f'{__class__.__name__}({self.__dict__})'
"""

class SuperTime:
    ...

@Repr_Decorator
class Time(SuperTime):
    def __init__(self, nome):
        self.nome = nome


@Repr_Decorator
class Planeta():
    def __init__(self, nome):
        self.nome = nome

br = Time('Brasil')
eua = Time('Estados Unidos')

terra = Planeta('Terra')
mart = Planeta('Marte')


print(br)
print(eua)

print(terra)
print(mart)