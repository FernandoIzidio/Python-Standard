"""
É UMA LIST comprehension feita em tuplas
É esgotavel, é um iterator
Pesa menos que outras extruturas de dados
Não possui repr e str definidos
Não possui indice, nem comprimento pois é um iterator
pode ser chamado com next

É uma extrutura muito boa para armazenar dados temporarios, ou seja é uma extrutura ideal para economizar espaço

Yield pausa e retorna/recebe um valor

send usado para fazer generator receber valores por yield, ou seja send envia valores para o yield generator
throw - lança uma exceção no generator
"""
from sys import getsizeof

numbers = (count for count in range(10))
numberslist = [count for count in range(10)]
print(numbers, getsizeof(numbers))

"""
Em termos de uso de memória, o gerador não mantém todos os elementos em memória de uma vez, ele produz os elementos conforme você itera, economizando memória. e por isso o getsizeof() não representa o tamanho do generator
"""
print(numberslist, getsizeof(numberslist))
"""
Todos os valores da lista são armazenados na memória, e por isso o getsizeof() - reflete o tamanho da lista em termos de espaço
"""


def example_generator():
    while True:
        received = yield

        print(f"Received: {received}")

    

numeros  = example_generator()
print(next(numeros))
numeros.send(4)
