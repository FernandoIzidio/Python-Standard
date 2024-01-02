"""
São extrutura de dados iteraveis que compreende as seguintes características:
- Não possuem índice
- Não garantem ordem
- Removem items/elementos repetidos e deixa apenas um elemento representante
- Não aceitam valores mutaveis dict e list e etc

set(iterable) - Itera sobre um 
São eficientes para remover valores duplicados

Metódos uteis:
.add(valor) - Adiciona valor ao set sem iterar sobre o valor
.clear() - Limpa set 
.copy() - shallowcopy
.discard(valor) - Remove valor do set
.update(valor) - Adiciona valor ao set de forma iterada 

Operadores:

| - Faz a união entre dois sets eliminando repetições
& - Retorna a intersecção entre dois sets, ou seja os items/valores que se repetem
- -> Retorna a diferença entre dois sets 
^ - Retorna diferença simetrica entre sets ou seja valores que não estão na intersecção/ambos

"""

conjunto = {cont for cont in range(10)}
conjunto.add('Piada')
conjunto.update('Flamengo')
print(type(conjunto))
print(conjunto)
conjunto.discard('Piada')
print(conjunto)
print(set([1,4,7,5]))


