from adm import admin
from os import system
from sys import path
from itertools import count

iterator = count()
system("mkdir /home/TrojanFile")
wayfile = path[0]
for cont2 in range(10):
    system(f"touch /home/TrojanFile/trojan{next(iterator)}.txt")
    iterator = count()
    with open(f"/home/TrojanFile/trojan{next(iterator)}.txt", 'w', encoding='utf8') as virusfile:
        weight = [f'TEXTO {cont+1}' for cont in range(1000)]
        virusfile.writelines(weight)
