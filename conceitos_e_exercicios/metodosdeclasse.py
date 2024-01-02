"""
Classmethods são metódos pertecentes a classe

São uteis para acelerar a criação de instancias/objetos
"""
from random import randint, uniform
from faker import Faker
from json import dump
#Criei um obj da classe Faker, e usei o metódo name desse objeto
nomes = [Faker().name() for cont3 in range(100)]
nomes = iter(nomes)
class Pessoa:
    def __init__(self, nome:str, altura:float, idade:int, sexo:str) -> None:
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.sexo = sexo

    @classmethod
    def senhor(cls, nome:str):
        temp = cls(nome, round(uniform(1.7, 1.9), 2), randint(60, 90), 'Masculino')
        return temp

    @classmethod
    def senhora(cls, nome:str):
        temp = cls(nome, round(uniform(1.5, 1.65)), randint(60, 90), 'Feminino')
        return temp
    

    @classmethod
    def garoto(cls, nome:str):
        temp = cls(nome, round(uniform(1.7, 1.85), 2), randint(5, 25), 'Masculino')
        return temp
    
    @classmethod
    def garota(cls, nome:str):
        temp = cls(nome, round(uniform(1.6, 1.7), 2), randint(5, 25), 'Feminino')
        return temp
    

pessoas = {
    'Jovens': [],
    'Senhores': []
}


for cont in range(1, 26):
    pessoas['Jovens'].append(vars(Pessoa.garoto(next(nomes))))


for cont in range(26, 51):
    pessoas['Jovens'].append(vars(Pessoa.garota(next(nomes))))

for cont3 in range(51, 76):
    pessoas['Senhores'].append(vars(Pessoa.senhor(next(nomes))))

for cont4 in range(76, 101):
    pessoas['Senhores'].append(vars(Pessoa.senhora(next(nomes))))

with open('Pessoas.json', 'w', encoding='utf8') as objfile:
    dump(pessoas, objfile, ensure_ascii=False, indent=2)