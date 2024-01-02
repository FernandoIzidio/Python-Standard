"""
Iterables e iterators são tipos de dados que podem ser iterados, mas que tem sutis diferenças

Todo iterator é um iterable, mas nem todo iterable é um iterator.

Um iterable contem os metódos:
    __iter__

Um iterator contem os metódos:
    __iter__
    __next__

=Ou seja principal diferença é que da para usar next em um iterator

-E outra diferença é que um iterator é consúmivel, ou seja após esgotado não é possivel reiterar sobre ele novamente

- Um iterator para ser exibido precisa ser consumido, normalmente o consumo é feito por uma lista, list(iterator), ou por partes com next(iterator)
 
-Um iterable para ter seus valores exibidos, pode ser inteiramente com print, parcialmente com fatiamento(numerico, ou string), ou pode ser parcialmente por meio de um iterador for


Extrutura:

iterator = x, y, z, a ...

iterable = [x, y, z]

Exemplos de iterables:
[...] ou (...) ou {...}
-Strings
-Tuplas
-Listas
-Dict
-Sets
-Range


Exemplos de Iterators:
(...), (...) ...
-Generator expressions / Generator functions
-Count
-Groupby
-Product
-zip
-Combinations e Permutation

Iterators precisam ser consumidos por uma lista, ou next, para terem seus valores exibidos

"""