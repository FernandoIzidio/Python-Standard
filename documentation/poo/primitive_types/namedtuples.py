
"""
Tipo de dados imutavel, pode ser chamado por chave númerica ou nomeada(fatiamento)
Não possui dict nem dir por isso não funciona dir nem vars


É o melhor extrutura de dados para registros em bases de dados, planilhas, arquivos csv e etc

Tem sintaxe parecida ao do enumerators

Funciona como uma dataclasse, mas sem metódos, ou seja named tuples é ideal para armazenar apenas dados

Objetos de classes named tuples tem metódos de objeto:
    - _asdict - funciona como vars
      tuple(obj) - Converte objeto para tupla

"""
from collections import namedtuple
Person = namedtuple('dataperson', ['Telefone', 'Nome', 'Idade', 'Sexo'], defaults=['Anônimo', 'Desconhecida', 'Não informado'])

obj = Person(Telefone=f"(34)99668-5165")
print(obj)

print(obj._asdict())
print(obj.Idade)
print(obj[3])
print(obj[0])