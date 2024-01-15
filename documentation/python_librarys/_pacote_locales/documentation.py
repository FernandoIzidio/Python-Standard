"""
Pacote usado para internacionalização do código
Permite ajustar a formatação de saída de acordo com a língua/codificação do país

Codificação é um tabela binária, que o SO usa para identificar os caracters e números


getlocale - Retorna as codificações/linguas disponiveis no SO

setlocale(lc**, codification:str) - Define a codificação/lingua para as categorias escolhidas, ou seja altera a codificação do sistema atual

LC_ALL - É um atributo que contem todas as categorias de uma lingua/SO
Power Shell - Get-WinSystemLocale - Retorna as codificações disponiveis no SO atual


locale.locale_alias - Retorna uma lista com todas as codificações/línguas disponiveis no SO


getencoding - Retorna a codificação do sistema atual


"""


from locale import getlocale, setlocale, LC_ALL, locale_alias, getencoding
from calendar import calendar
from os import system

print(getlocale())
print(getencoding())
setlocale(LC_ALL, 'english')

print(calendar(2022))


LOCAL = locale_alias #Todas as linguas disponiveis no SO



setlocale(LC_ALL, '')#Alterei todas as categorias de locale, pra codificação/lingua do sistema atual

print(calendar(2022))
