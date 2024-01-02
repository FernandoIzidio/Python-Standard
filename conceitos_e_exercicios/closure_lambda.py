from functools import partial
"""
Closure são funções que retornam outras funções como valor
"""



def executa(function, *args):
    return function(*args)

def cria_multiplicador(const):
    def interna(numero):
        return numero * const
    return interna

dobra = executa(lambda const: lambda num: const*num, 2)
quintuplo = lambda const: lambda num: const*num
print(quintuplo(5)(25))
print(dobra(8))

triplo = cria_multiplicador(3)
print(triplo(8))


quadruplo = partial(lambda x, y: x*y, 4)
print(quadruplo(10))

somatudo = partial(lambda initial_value, *args: initial_value+ sum(args), 0)

print(somatudo(8, 7, 48, 487))