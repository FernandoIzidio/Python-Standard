"""

Quer dizer que no Python, uma classe pode gerar várias outras classes.
Herança simples:
Animal -> Mamifero -> Humano -> Pessoa -> Cliente


Herança múltipla e mixins
Log -> FileLog
Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Cliente(Pessoa, FileLog)

-Mixins:
Classe que não tem pertence a hierarquia de uma família de classes


# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
Python 3 usa C3 superclass linearization
para gerar o mro.

Ordem de resolução de metódos em herança multipla diamante(opcional)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos:
Use o método de classe Classe.mro(), ou o atributo __mro__ 

class(x, y ....) Ele vai procurar o metódo primerio na child class/ classe atual, e se não achar, vai na primeira classe que ele herda x, e se não achar vai pra y, e se não achar, vai para a parent class master
"""


class A:
    def __init__(self) -> None:
        ...

    def identidade(self):
        print('Objeto pertencente a classe A')

class B(A):
    def identidade(self):
        super().identidade()
        print('Objeto pertencente a classe B')
        

        
class C(A):

    def identidade(self):
        super().identidade()
        print('Objeto pertencente a classe C')


class D(C, B):

    def identidade(self):
        super().identidade()
        print('Objeto pertencente a classe D')

        
testobject = D() 
print(D.mro())
testobject.identidade()
