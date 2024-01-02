"""
Extrutura de dados muito util para enumerar um grupo de coisas

enum(classname, keys/values ou [keys:valuesdefault])
Enumerators começam a contagem a partir do 1
"""
from enum import Enum
cores = Enum('Collors', {'Vermelho': 1, "Azul": 2, 'Amarelo': 3})
print(cores)
print(cores.Amarelo)
print(cores(1)) #Selecionei o primeiro atributo do enumerator
print(cores.Amarelo.name) # Name retorna a chave de um membro
print(cores(1).value) # Value retorna o valor de um membro
print(cores.Amarelo.__class__.__name__) # Class name retorna o nome da classe do enumerator