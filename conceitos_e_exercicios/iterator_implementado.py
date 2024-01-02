"""
Implementando protocolo do iterator, com os metódos e atributos essenciais que o compõe
-Qualquer objeto/protocolo pode ser personalizado e implementado em python

__getitem__(self) - Permite que o valor de uma extrutura de dados seja retornado por chave númerica ou nomeada
extru[num]
extru[chave]

__len__(self) - Torna uma extrutura de dados medivel por tamanho que é dado por número de itens
retornando o ultimo valor de indice

__setitem__() - Permite que o usuário atribua valor a uma lista por meio do indice

__iter__ - Deve retornar o próprio objeto

__next__ - Deve retornar o proximo valor da lista, e se o próximo indice for maior ou igual ao indice de comprimento raise stopiteration, para o for localizar onde termina o iterable

A extrura for precisa receber um erro para parar a iteração e saber quando é o fim de uma lista
antes do for receber a excessão/erro e parar a iteração é possivel zerar o nextindice para o iterable possa ser novamente iterado

"""
from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self) -> None:
        self.mochila = {}
        self.indice = 0
        self.nextindice = 0

    
    def __getitem__(self, indice):
        return f'{self.mochila[indice]}'

    def append(self, *valor):
        for item in valor:
            self.mochila[self.indice] = item
            self.indice += 1

    def __len__(self) -> int:
        return self.indice

    
    def __str__(self) -> str:
        return f'{self.mochila}'
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({vars(self)})'
    
    
    def __setitem__(self, indice, valor):
        self.mochila[indice] = valor

    def __iter__(self):
        return self

    def __next__(self):
        #O for só para a iteração se o erro for lançado
        if self.nextindice >= self.indice:
            self.nextindice = 0
            raise StopIteration
        
        valor = self.mochila[self.nextindice]
        self.nextindice += 1
        return valor

lista = MyList()

lista.append('Truco')
lista.append('Flapiada')
print(lista)
print(repr(lista))
print(lista[0])
print(len(lista))

lista2 = MyList()
lista2.append('Truco')
lista2.append('Flamerda', 'Bené')
print(lista2)
lista2[len(lista2)] = 'TRUCOOOOOO'
print(lista2)
for item in lista2:
    print(item)
