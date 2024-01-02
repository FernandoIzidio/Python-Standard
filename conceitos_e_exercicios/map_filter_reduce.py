from functools import reduce
from os import system
from itertools import count
graph = count()
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtosaumentados = sorted(list(map(lambda dicionario: {**dicionario, 'preco': round((dicionario['preco'] * 1.20), 2)}, produtos)), key=lambda dicionario: dicionario['preco'])

#Peguei chave preço de cada dicionário e adicionei ao acumulador
print(*produtosaumentados, sep='\n')
print(reduce(lambda acumulador, dicionario: dicionario['preco'] + acumulador, produtosaumentados, 0))
input(f'[{next(graph)+1}]:')
system('clear')


produtosaumentados2 = sorted(list(map(lambda dicionario: {**dicionario, 'preco': dicionario['preco'] * 4}, produtos)), key=lambda dicionario: dicionario['preco'], reverse=True)



print(*produtosaumentados2, sep='\n')
print(f"A soma dos valores equivalem a: {round(reduce(lambda acumulador, dicionario: acumulador + dicionario['preco'], produtosaumentados2, 0), 2)}")
input(f'[{next(graph)+1}]:')
system('clear')


produtosfiltrados1 = list(filter(lambda dicionario: dicionario['preco'] > 80, produtosaumentados))

print(*produtosfiltrados1, sep='\n')
input(f'[{next(graph)+1}]:')
system('clear')

produtosfiltrados2 = list(filter(lambda dicionario: dicionario['preco'] > 200, produtosaumentados2))

print(*produtosfiltrados2, sep='\n')
input(f'[{next(graph)+1}]:')
system('clear')