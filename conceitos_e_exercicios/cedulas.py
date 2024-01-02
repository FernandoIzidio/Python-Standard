from enum import Enum
from os import system
from time import sleep
ced = Enum('Cedulas', {'Quinhentos': 500, 'Duzentos': 200, 'Cem': 100, 'Cinquenta': 50, 'Vinte': 20, 'Dez': 10, 'Cinco': 5, 'Dois': 2, 'Um': 1})

while True:
    try:
        valor = float(input('Digite um valor: '))
    except (TypeError, ValueError):
        print('Erro: Digite apenas números')
    else:
        break

for cedula in ced._value2member_map_.keys():
    numerocedulas, valor = divmod(valor, cedula)
    print(f'{numerocedulas} cédulas de R$ {cedula},00')