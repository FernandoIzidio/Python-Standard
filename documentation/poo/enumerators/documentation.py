"""
Enumerators são uteis quando se precisa enumerar um conjunto de opções
"""
from enum import Enum

class Geometric(Enum):
    TRIANGULO = '3 Lados'


print(Enum('triangulos', {'quadrado': 'especial'}).quadrado.value)
print(Enum('triangulos', {'quadrado': 'especial'})('especial').name)


for form in Geometric:
    print(form.__class__.__name__,  form,  form.name, form.value, sep='\n')