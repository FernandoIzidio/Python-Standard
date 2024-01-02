"""
Metódo rápido para criar novas listas a partir de iterables(iteraveis)

mapeamento- Nunca altera tamanho da lista, apenas altera valores da lista
filtro - Altera tamanho da lista, seguindo uma condição

Ordem de aninhamento:

x = [string.upper() for list in y for string in list]
-Primeiro é feito a iteração em todas as listas de y
-Logo depois é feito a iteração em todas as strings de cada lista de y

Outro caso:

z = [{**dicionario} for dicionario in list({...} ...)]
- É feito a iteração sobre cada dicionario da lista
- Logo em seguida cada dicionario tem suas chaves e valores desempacotados em um novo dicionário

"""
from random import randint
from os import system
from time import sleep

x = 487.5987
print(round(x, 2))

produtosimg = [{'Nome': f'Produto {cont+1}', 'Preço': f'R${randint(20, 100)*3.19:.2f}'.replace('.', ',')} for cont in range(10)]

print(*produtosimg, sep='\n')
print(len(produtosimg))
input('Next:')
system('clear')

produtos = [{'Nome': f'Produto {cont+1}', 'Preço': randint(500, 1000)} for cont in range(10)]


print(*produtos, sep='\n')
input('Next:')
system('clear')

prodaumento = [{**dicionario, 'Preço': float(f"{dicionario['Preço'] * 1.39:.2f}")} for dicionario in produtos]

print('')
print(*prodaumento, sep='\n')
input('Next:')
system('clear')


print('')

prodfiltro = [{**dicionario, 'Preço': f"R${dicionario['Preço']}".replace('.', ',')} for dicionario in prodaumento if dicionario['Preço'] >= 1000]

print(*prodfiltro, sep='\n')
input('Next:')
system('clear')

cordenadas = [(x, y) for x in range(10) if x % 2 != 0 for y in range(10) if y % 2 == 0]
print(*cordenadas, sep='\n')
print(len(cordenadas))