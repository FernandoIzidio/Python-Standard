"""
Listas são extrutas de dados iteraveis que tem como característica:
-São mutaveis, ou seja pode remover ou adicionar items após a declaração
-Possuem indice númerico

Principais metódos:
.index(valor) - Retorna a posição do valor dentro da lista
.count(valor) - Retorna quantas vezes determinado valor se repetiu dentro da lista
.append(valor) - Adiciona valor a lista como último item
.insert(pos, valor) - Inseri valor a lista de acorda com a posição
.clear() - Limpa a lista
.copy() - Retorna uma shalow copy da lista
.pop([pos]) - Por padrão remove o ultimo item da lista, mas pode remover o item de acordo com a pos
.remove(valor) - Remove determinado valor da lista
.extend(lista) - Adiciona todos os items de uma outra lista, a essa lista
.sort(key) - Ordena uma lista em ordem crescente por padrão, pode receber o uma chave para ordenar



Observações importantes

Deepcopy - Copia profunda de uma lista ou seja mesmo que eu altere valores mutaveis de uma lista, a outra lista seguira a mesma

Shallowcopy - Copia rasa de uma lista, ou seja se alterar um item/valor mutável de uma lista a outra lista também sera alterada

Lista = Lista2 - Ligação entre listas, se eu alterar uma qualquer uma das duas listas, a mudança valera para as duas

"""

#Quando uma váriavel recebe vários valores, e o tipo de extrutura de dados da váriavel não é declarado, essa váriavel por padrão será uma tupla, que empacotara todos os valores

var = ['chave', 'valor1'], ['chave', 'valor1'], 787
print(var)
print(type(var))

listaimpa = [cont for cont in range(1,11) if cont % 2 != 0]
listapar = [cont for cont in range(1,11) if cont % 2 == 0]
listanum = []
listanum.extend(listaimpa)
listanum.extend(listapar)
listanum = sorted(listanum)
print(listaimpa)
print(listapar)
print(listanum)
print(type(listaimpa))