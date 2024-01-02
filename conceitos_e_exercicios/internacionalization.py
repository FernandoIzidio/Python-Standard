"""
setlocale(LC_ALL, "") - faz a tradução dos pacotes e modulos importados neste módulo, e traduz para linguagem da machine local
"""

from locale import getlocale, setlocale, LC_ALL
from calendar import calendar


setlocale(LC_ALL, '')

pan =  calendar(2020)
print(pan)

print(getlocale())