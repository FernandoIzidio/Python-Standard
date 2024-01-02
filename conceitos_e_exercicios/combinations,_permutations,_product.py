"""
combinations - Ordem não importa e não altera tamanho da lista
-Combination é a combinação entre todos os elementos da lista
permutations - Ordem importa e altera tamanho da lista
-Combination é a combinação entre todos os elementos da lista

product - Combinação entre várias listas
"""
from itertools import combinations, permutations, product
from os import system
pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]


print(*list(combinations(pessoas, 2)), sep='\n')
input('Next:')
system('clear')

print(*list(permutations(pessoas, 2)), sep='\n')
input('Next:')
system('clear')

print(*list(product(*camisetas)), sep='\n')