"""
Tipo de dado mutavel
iterable

Methods and operations usefull:
    lista.append(value) - Adiciona valor na ultima posição da lista
    lista.insert(pos, value) - Adiciona valor na lista na posição escolhida
    lista.clear() - Limpa lista
    lista.copy() - Retorna uma shallow copy da lista(copia profunda dos imutavies, e referenciamento dos tipos mutaveis)
    lista.extend(iterable) - Itera sobre uma outra lista e adiciona item a item na lista atual
    lista1 + lista2 - faz a mesma coisa que lista.extend, itera sobre uma lista, adicionando cada item dessa lista na lista atual
    lista.index(value) - Retorna a posição de um valor
    lista.remove(value) - Remove primeira ocorrência de um valor
    lista.pop(pos=-1) - Reomove um item de uma lista de acorda com a posição
    lista.reverse() - Inverte a ordem de uma lista
    lista.sort() -> None - Ordena os itens de uma lista
    sorted(lista) -> Retorna uma copia da lista ordenada
    lista * int-> Repete os itens da lista o numero de int, ou seja dobra, triplica e etc o tamanho da lista com os mesmo itens
    
    lista *= int -> Dobra, triplica, e etc o tamanho da lista, e modifica o tamanho da propria lista


"""
dados = [1 for count in range(10)]
dados2 = [2 for count in range(10)]
dados *= 10
print(dados)
print()
print(dados +dados2)
