"""
-Empacotamento:

def func(*args, **kwargs):
    return ...

-*args vai empacotar todos os argumentos posicionais em uma lista
-**Kwargs vaai empacatar todos os argumentos nomeados em um dicionário

-Desempacotamento

list = [...]
dic = {...}

print(*list)
-*list vai desempacotar todos os itens da lista, e passar item por item, como argumentos. Ex:
print(item1, item2, item3...)

print(**dic)
-**dic vai desempactor todos as chaves e valores de dic, e passar cada par como argumento da função. Ex:
print(chave=valor, chave2=valor2...)
"""
from random import randint
from itertools import count

iterator = count()

produtos = [{'Nome': f'Produto {next(iterator)+1}', 'Preço': f'R${randint(100, 500)*2.54:.2f}'.replace('.', ',')} for count in range(10)]

print(*produtos, sep='\n')