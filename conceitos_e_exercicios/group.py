"""
Agrupa dicionários/listas por valores de chave repetidos

-os dicionários que tem determinada chave ficam agrupados em uma chave e os que tem outra ficam em outra chave.
"""

from itertools import groupby
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
alunos.sort(key=lambda dicionario: dicionario['nota'])
melhoresalunos = groupby(alunos, key=lambda dicionario: dicionario['nota'])

for chave, grupo in melhoresalunos:
    print(chave)
    print(*list(indiv['nome'] for indiv in grupo), sep='\n')