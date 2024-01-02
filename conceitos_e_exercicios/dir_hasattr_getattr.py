"""
dir(object) - Retorna todos os atributos e metódos de um objeto
hasattr(obj, atr) - Verifica se um obj tem determinado atributo/metódo e retorna valor bool
getattr(obj, atr/met) - Retorna o metódo/attr de um obj se o obj tiver esse attr, metodo
"""


from Option_Error import OptionError

def verifica(obj):
    if hasattr(obj, '__iter__') and hasattr(obj, '__next__'):
        print(f'{obj.__class__.__name__} é um iterator')
    elif hasattr(obj, '__iter__'):
        print(f'{obj.__class__.__name__} é um iteravel')
    else:
        raise OptionError



x = [cont for cont in range(10)]

print(dir(x))
y = (cont for cont in range(5))

z = 487
x = 'Flamengo Piada'

metodo =  getattr(x, 'upper')

print(metodo)

try:
    verifica(x)
    verifica(y)
    verifica(z)
except OptionError:
    print('Erro: Digite uma opção válida')



