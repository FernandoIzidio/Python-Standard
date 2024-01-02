"""
Tipo de dado mutavel iterable

Regras:
    Não aceita valores mutaveis.
    Não tem ordem
    Não tem indice
    Apenas valores únicos

Metódos uteis:  
    set(iterable) - Adiciona todas as fatias/items de um itebla ao conjunto
    update(iterable) - Adiciona items/fatias ao set de forma iterada
    add(element) - Adiciona um elemento ao conjunto
    clear - Limpa conjunto
    copy - Faz uma deep copy do conjunto, até porque conjuntos só aceitam valores imutaveis
    pop - Remove primeiro item do set, na ordem que vir
    discard(value) - Remove valor do set
    union(set) ou | _> set- Faz a união com outro set(Une todos os elementos de ambos sets, sem repetir)
    conjunto.interseccion ou & -> set - Faz a intersecção entre dois conjuntos(Elementos que se repetem)

    conjunto.difference ou conjunto - conjunto2 -> set - Tira os elementos do outro set, e retorna um set sem os elementos do outro set

    conjunto.difference_update - Atualiza o set atual remove os valores que estão no outro set


    conjunto.symetric(conjunto2) ou conjunto ^conjunto2 - Retorna set com valores que não estão presentes em ambos ao mesmo tempo, ou seja retorna set com valores que não estão na intersecção

    conjunot.symetric_update() - Atualiza o set atual, removendo valores que são intercção com outro conjunto
    
    """

conjunto = set('ABC')
print(len(conjunto))
conjunto.add('D')
conjunto2 = conjunto.copy()
print(conjunto)
conjunto2.add('I')
conjunto.update('EFG')
print('')

print(conjunto,'X', conjunto2)
print(conjunto.union(conjunto2))
print(conjunto2 | conjunto)
print('')
print('')
print(conjunto.intersection(conjunto2))
print(conjunto & conjunto2)
print('')
print('')
print(conjunto2 - conjunto)
print(conjunto2.difference(conjunto))
print('')
print('')
print(conjunto ^conjunto2)
print(conjunto.symmetric_difference(conjunto2))
print('')
print('')
conjunto.pop()
print(conjunto)
conjunto.pop()
print(conjunto)
conjunto.pop()
print(conjunto)
conjunto.discard('C')
print(conjunto)

