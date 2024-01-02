"""
Strings é um tipo de dado iteravel ou seja que pode ser repartido letra por letra

Metódos importantes de strings:
.capitalize() - Converte primeira letra para maiusc e resto para minusc
.upper() - Converte string para maiúsculo
.lower() - Converte string para minúsculo
.count(valor) - Conta quantas vezes um valor se repete dentro de um string
.index(valor) - Retorna a posição de um valor dentro de uma string, e se o valor não for encontrado retorna ValueError
.find(valor) - Retorna a posição de um valor dentro de uma string, e se o valor não for encontrado retorna -1
.strip() - Tira os espaços antes e depois da string
.split(sep) - Separa a string de acordo com o valor do separador, e pega cada parte repartida e retorna em uma lista
.isdecimal() - Verifica se a string é um número natural
.isdigit() - Verifica se a string é um número inteiro
.isnumeric() - Verifica se a string é um número inteiro/fração/númeroromano+
.replace(old, new) - Troca parte de uma string old e substitui pela parte new -> Retorna a string nova
sep.join(iterable) - Junta os itens/partes de um iteravel, e transforma em uma string separando cada parte com o valor do separador - Retorna string
"""

x = 'R$784.24 R$483.48 R$475.14'
x = x.replace('.', ',')
precos = x.split(' ')
print(precos)
texto = ' '.join(precos)
print(texto)