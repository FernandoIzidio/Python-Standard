"""
Shallow copy - Copia rasa, se houver alteração nos valores mutaveis, ambos os dicionários/listas são alterados
Copiam valores imutaveis, e faz a ligação/link dos valores mutaveis

deep copy - Uma alteração de um não altera ou outro

ligação dic/list = dic/list - Uma alteração de um sempre altera o outro


"""


from copy import deepcopy


d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()

d2['c1'] = 5
d2['l1'][1] = 8

print(d1)
print(d2)

d2 = deepcopy(d1)

d2['l1'][0] = 50

print(d1)
print(d2)