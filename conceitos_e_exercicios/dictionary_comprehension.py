"""
Maneira rápida de criar novos dicionários
"""
from json import load
from os import system
from time import sleep
from random import randint

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}


print(produto)

print('')
dc = {chave.capitalize(): valor.upper() if isinstance(valor, str) else valor * 3 for chave, valor in produto.items()}

print(dc)
input('next')
with open('dados.json', 'r', encoding='utf8') as arquivo:
    dados = load(arquivo)

system('clear')
produtos = [{**dicionario, chave.capitalize(): valor.upper() if isinstance(valor, str) else f'R${valor:.2f}'.replace('.', ',')}for dicionario in list({'Nome': lista[0], 'Preco': float(f'{randint(1, 500) * 2.54:.2f}'), 'Categoria': lista[1]} for lista in dados) 
            for chave, valor in dicionario.items()]

print(*produtos, sep='\n')