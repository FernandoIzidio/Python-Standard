"""
Codificação é um tabela binária, que o SO usa para identificar os caracters e números

Permite ajustar a formatação de saída de acordo com a língua/codificação do país

Pacote usado para internacionalização do código
getlocale - Retorna as codificações/linguas disponiveis no SO
setlocale(lc**, codification:str) - Define a codificação/lingua para as categorias escolhidas
LC_ALL - É um atributo que contem todas as categorias de uma lingua/SO
Power Shell - Get-WinSystemLocale - Retorna as codificações disponiveis no SO atual
locale.locale_alias - Retorna uma lista com todas as codificações/línguas disponiveis no SO
getencoding - Retorna a codificação do sistema atual


"""


from locale import getlocale, setlocale, LC_ALL, locale_alias
from calendar import calendar
from os import system

print(getlocale())
setlocale(LC_ALL, '')

print(calendar(2022))


LOCAL = locale_alias
for codification in LOCAL:
    print(codification)
input('next')
system('cls')

setlocale(LC_ALL, '')#Alterei todas as categorias de locale, pra codificação/lingua do sistema atual