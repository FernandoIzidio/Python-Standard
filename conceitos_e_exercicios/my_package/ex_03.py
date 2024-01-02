produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
from os import system

print(*produtos, sep='\n')
input('Next:')
system('clear')

novos_produtos = [{**dicionario, 'preco': float(f"{(dicionario['preco'] * 1.10):.2f}")} for dicionario in produtos]

print(*novos_produtos, sep='\n')
input('Next:')
system('clear')


produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda dicionario: dicionario['nome'])

print(*produtos_ordenados_por_nome, sep='\n')
input('Next:')
system('clear')

produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda dicionario: dicionario['preco'], reverse=True)

print(*produtos_ordenados_por_preco, sep='\n')
input('Next:')
system('clear')

print('Encerrando...')