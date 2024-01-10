"""
Enumerators são uteis quando se precisa enumerar um conjunto de opções

Enum(enumarationName, {atributos:valor})
enumarationName, sera usado na hora de montar o repr de um membro, ao obter um membro, o nome do membro sera concatenado ao nome da enumeração
"""
from enum import Enum

class Geometric(Enum):
    TRIANGULO = '3 Lados'


print(Enum('triangulos', {'quadrado': 'especial'}).quadrado.value)
print(Enum('triangulos', {'quadrado': 'especial'})('especial').name)

print('\n')
print(Enum("triangulos", {"bola": "especial"}).bola)
print('\n')

for membro in Geometric:
    print(membro.__class__.__name__,  membro,  membro.name, membro.value, sep='\n')