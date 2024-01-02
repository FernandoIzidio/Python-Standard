"""
Funções que modificam outras funções

def decorator(func):
    print(...) - Essa modificação só vai ser exibida uma vez, na chamada do decorator
    def interna(*args, **kwargs):
        print(...) - Essa modificação vai aparecer em todas as chamadas da função
        return func(*args) 
    return interna

Decorators são funções que modificam outras funções
Parte principal do decorator recebe a função
Parte interna(função interna do decorator), modifica a função

No decorator a função interna vai fazer toda a modificação de comportamento da função, e depois vai chamar a função antiga para que ela não seja substituida.

Quando a função antiga não é chamada na função interna, a função interna substitui a função antiga
"""

def fabrica_de_decorators(a, b, c, cond):
    print(a, b, c, sep='\n')
    def decorator(func):
        print('Modificando a função com o decorador')
        def interna(*args, **kwargs):
            for arg in args:
                if cond == True:
                    check(arg, str)
                else:
                    check(arg, (int, float))
            print('Bom dia(Modificação)')
            return func(*args, **kwargs)#Transforma a função interna na função a ser decorada
        return interna#Retorna a função modificada
    return decorator #Retorna decorator modificado
def check(arg, classe):
    if not isinstance(arg, classe):
        raise ValueError(f'Erro: Forneceu argumento de tipo invalido.')


@fabrica_de_decorators(8, 5, 3, True)
def invertestring(string):
    return string[::-1]


print(invertestring('roma'))

print(invertestring('amor'))

print(invertestring('Carro'))

"""
dec = fabrica_de_decorators(5, 7, 487, False)
multiplica = dec(lambda x, y: x*y)
"""

multiplica = fabrica_de_decorators(5, 7, 487, False)(lambda x, y: x*y)

print(multiplica(7, 8))
print(multiplica(5, 4))
print('')
print('')
print(invertestring(87))
