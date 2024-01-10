
"""
Named tuples é como se fosse uma dataclasse mas apenas para dados, as named tuples tem uma sintaxe bem parecida aos enumerators

São muito uteis para registros de bases de dados, arquivos csv, pois dão dados imutaveis


Metódos de objetos de classes NAMED TUPLES:
    objeto.asdict() - Converte uma namedtuple para dicionário, atriubuto nome e valor, serão as chaves e valores de dicionário
    tuple(objeto) - Converte para tupla um objeto named tuple

objetos named tuples são fatiaveis, ou seja tem o __getitem__ implementado, porém não possuem o metódo __dict__ portanto não suportam vars()

named tuple vai retornar uma classe, com __init__ definido, e é uma classe apenas de dados, pois essa classe só vai ter atributos
"""

from collections import namedtuple
from random import randint

dados = namedtuple('Pessoas', ['Nome', 'Idade', 'Sexo', 'Telefone'], defaults=[None, None, None, f'({randint(11, 100)}){randint(9000, 9999)}-{randint(11111, 99999)}'])

d1 = dados('Tulio', 18, 'Masculino')

print(tuple(d1), sep='\n')
print(d1[1])
print(d1[3])
print(d1.Nome)