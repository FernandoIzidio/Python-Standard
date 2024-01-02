"""
Funções lambdas são funções anônimas que não tem nome, e precisam ser chadas normalmente por meio de auxilio de outras funções
Extrutura:

Lambda   a, b     :   a+b
      Parametros    Retorno

Partial passa os argumetos de uma função de forma parcial e retorna outra função como valor, ou seja funciona como uma closure

"""
from functools import partial

def executa(func, *args):
    return func(*args)

triplica = executa(lambda const : lambda num : const * num, 3)

print(triplica(8))


quintuplo = partial(lambda const, num: const * num , 5)
print(quintuplo(30))
