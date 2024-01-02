from enum import Enum
from decimal import Decimal

bills = Enum('nota', ['100', '50', '20', '10', '5', '2'])
coins = Enum('moeda', ['1', '0.50', '0.25', '0.10', '0.05', '0.01'])

def show_converted_value(value: Decimal, formato: Enum) -> Decimal:
    print(f'{formato.__name__}'.upper() + 'S:')
    for membro in formato:
        numpart, value = divmod(value, Decimal(membro.name))
        print(f'{int(numpart)} {formato.__name__}(s) de R$ {float(membro.name):.2f}')
    return value
value = Decimal(input())

remaining_value = show_converted_value(value, bills)
coins = show_converted_value(remaining_value, coins)