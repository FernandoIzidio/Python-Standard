
"""
Para implementar qualquer sequence, basta identificar quais são os metódos e atributos essenciais que compõem a sequence


__iter__ - Implementa iterables, deve retornar o prório self, objeto
__iter__ + __next__ - Implementa iterators


collections.abc, contém várias classes abstratas com os metódos e atributos necessários para implementar cada sequence
"""

from collections import abc
from faker import Faker
from random import choice
db = Faker()
class MyPersonSequence:
    def __init__(self) -> None:
        self.data = {}
        self.lenght = 0
        self.index = 0

    def append(self, value):
        self.data[self.lenght] = value
        self.lenght += 1

    def __len__(self):
        return self.lenght
    
    def __bool__(self):
        if self.data:
            return True
        return False
    
    def __getitem__(self, indice):
        return self.data[indice]
    

    def __setitem__(self, indice, value):
        self.data[indice] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.lenght:
            raise StopIteration
        
        item = self.data[self.index]
        self.index += 1
        return item

    def __str__(self) -> str:
        return f'{vars(self)["data"]}'
    


print('True' if MyPersonSequence() else 'False')

dicionario  = MyPersonSequence()

for count in range(10):
    dicionario.append([lambda: choice([ db.name(), db.email(), f'({db.random_int(1,100)}){db.random_int(9000, 9999)}-{db.random_int(11111, 99999)}'])][0]())

for item in dicionario:
    print(item)

print("\n\n\n")
print(dicionario[0])