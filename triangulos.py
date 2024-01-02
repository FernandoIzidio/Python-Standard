from decimal import Decimal
from typing import Callable
lados = list(map(Decimal, input().split(' ')))

check_triangle_existence : Callable[[Decimal, Decimal, Decimal], bool] = lambda x, y, z: True if x < y + z and y < x + z and z < x + y else False 

if check_triangle_existence(*lados):
    if any(lado**2 == (lados[(pos + 1)%len(lados)]**2 + lados[(pos + 1)%len(lados)]**2) for pos, lado in enumerate(lados)):
            print('TRIANGULO RETANGULO')
    elif any(lado**2 > (lados[(pos + 1)%len(lados)]**2 + lados[(pos + 2)%len(lados)]**2) for pos, lado in enumerate(lados)):
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')

    if [lado == lados[0] for lado in lados].count(False) == 1:
        print('TRIANGULO ISOSCELES')
    elif all(side == lados[0] for side in lados):
        print('TRIANGULO EQUILATERO')
else:
    print('NAO FORMA TRIANGULO')