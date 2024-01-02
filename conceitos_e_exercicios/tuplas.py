"""
Tuplas são iteraveis que contém as seguintes características:
- São imútaveis, após a declaração não é possível remover nem adicionar items a tupla
-Possui índice númerico
-Não aceitam valores mutaveis

Metódos importantes:
.count(valor) - Retorna quantas vezes determinado valor se repetiu na tupla
.index(valor) - Retorna a posição do valor dentro da tupla


"""


tupla = tuple(f'Pessoa {cont+1}' for cont in range(0,10))

print(tupla)
print(tupla[0])
print(type(tupla))
print(*list('Pessoa' in palavra for palavra in tupla), sep='|')
print(tupla.count('Pessoa 1'))
print(tupla.index('Pessoa 6'))
