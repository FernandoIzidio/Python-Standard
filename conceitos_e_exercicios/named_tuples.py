"""
Named Tuples:
-Extrutura de dados imutavel
-iteravel
-imutaveis como as tuplas

Named tuplmas são tupla com nome para valores.

São úteis para criar classes sem metódos, apenas com atributos, ou armezenar valores de um banco de dados

namedtuple(nomedaclasse, ["attr", "attr2"]) -> cria uma classe, que quando instaciada retorna um obj

nomedaclasse- define qual o nome da classe
attrr[...] - Define os nomes dos atributos da classe

os valores dos atributos podem ser chamados por número, e por chave:

obj.chave
obj[pos]

defaults = []
define valores padrões para atributos
"""

from collections import namedtuple
from typing import NamedTuple

cartas = namedtuple('Carta_Magica', ['Número', 'Naipe'], defaults=['X', 'Magic'])
as_espada = cartas(1, 'espada')
print(as_espada)
print(as_espada.Número)
print(as_espada.Naipe)
print(as_espada[1])

ouro = cartas()
print(ouro)
print(ouro._asdict())

class Pessoa(NamedTuple):
    nome: str = 'Anônimo'
    idade: int = 'Desconhecida'

p1 =  Pessoa()
print(p1)
print(p1._asdict())
print(p1.nome)