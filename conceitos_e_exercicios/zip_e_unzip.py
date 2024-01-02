from itertools import zip_longest

states = ['Salvador', 'Ubatuba', 'Belo Horizonte']
cities =['BA', 'SP', 'MG', 'RJ']

def unir(iterable1, iterable2):
    inter = min(len(iterable1), len(iterable2))

    lista = [(iterable1[count], iterable2[count]) for count in range(inter)]

    return lista

print(unir(cities, states))
print(list(zip(cities, states)))
print(list(zip_longest(cities, states, fillvalue='Sem cidade')))

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

listasoma = [x+y for x,y in zip(lista_a, lista_b)]
print(lista_a)
print(lista_b)
print(listasoma)