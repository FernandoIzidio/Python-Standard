
"""
@ABSTRACT Class method sempre sera o decorator mais interno

Para implementar um setter em uma property abstrata o setter tem que descer junto da child class, ou seja só é possivel implementar um setter se a property tiver implementada


para implementar o um setter abstrato, é preciso usar o namespace da property da parent class na hora de implementar esse setter abstrato para a property
"""
from abc import abstractclassmethod
class RandomClass:
    def __init__(self, nome) -> None:
        self.nome = nome

    @property
    @abstractclassmethod
    def getnumber(self):...


class ChildClass(RandomClass):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.get_number = 5

    @property
    def getnumber(self):
        return self.get_number 
    
    @getnumber.setter
    def getnumber(self, valor):
        self.get_number = valor


obj =  ChildClass('truco')
print(obj.getnumber)
obj.getnumber = 8
print(obj.getnumber)

class RandomNumber:
    def __init__(self) -> None:
        self.get_number = 12

    @property
    def getnumber(self):
        return self.get_number
    

    @getnumber.setter
    @abstractclassmethod
    def getnumber(self):...


class ChildNumber(RandomNumber):

    @RandomNumber.getnumber.setter
    def getnumber(self, valor):
        self.get_number = valor

obj2 = ChildNumber()
print(obj2.getnumber)
obj2.getnumber = 23
print(obj2.getnumber)