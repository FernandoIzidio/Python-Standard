"""
Generator é uma extrutura de dados do tipo iterator que tem as seguintes características:
- Não consome espaço na memória
- Não possui índice
- É esgotavel
- Para ter seus valores exibidos é preciso ser consumido em uma lista, ou chamar o next(generator)
- Os argumentos fornecidos para os parâmetros, só são apagados da memória, quando a execução da função termina(return)


yield from function/generator
-Consome toda a função, ou generator, até o fim da execução deles(a), e pausa a função atual
"""
from random import randint
from sys import getsizeof
from os import system


gerador =  (cont for cont in range(100000))
lista = [cont for cont in range(100000)]

print(getsizeof(gerador))
print(getsizeof(lista))

print(gerador)
print(next(gerador))
print(next(gerador))
#print(list(gerador))


def intervalo(ini, fim):
    print('Executando intervalo número 1')
    while ini < fim:
        print(f'Iterada numero {ini}')
        yield ini 
        ini += 1

#Yield from esgota um iterator/generator function e depois executa a função atual


def intervalo2(ini, fim):
    yield from intervalo(ini, fim/2)
    print('Executando intervalo número 2')
    new = fim / 2
    while True:
        print(f'Iterada numero {round(new, 0)}')
        yield new
        new += 1
        if new >= fim:
            return ''
        
def executa_gen(gen, *args):
    print('Executando o generator')
    yield from gen(args[0], args[1])

    print('Executando o genrator principal')
    for arg in args[2::]:
        yield arg * 2



x = intervalo2(1, 10)
print(next(x))
print(next(x))
print(list(x))

generatorexpression = executa_gen(intervalo2, 0, 8, *list(randint(1, 30) for count in range(10)))
input('Next:')
system('clear')


print(next(generatorexpression))
print(next(generatorexpression))
print(next(generatorexpression))
print(next(generatorexpression))
print(list(generatorexpression))