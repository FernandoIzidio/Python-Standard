"""Decimal
Número perfeitos quando se quer uma precisão muito grande em representar números, é o tipo mais preciso de python

Metódos uteis:
    - obj.as_integer_ratio()- Retorna fração mais próxima de representar o número
    - obj.as_tuple() - 'Retorna o repr do número', o sinal dele(0 FALSE NÃO TEM SINAL, 1 TRUE TEM SINAL NEGATIVO), o número de digitos, e o expoente
    - obj.to_integral - Converte um número para inteiro
    - obj.compare(other) - -1 se obj for menor que other, 0 se for igual, 1 se obj for maior qeu other


    """
from decimal import Decimal

numero = Decimal(459.5600000000000 ** 4)


print(numero.as_integer_ratio())
print(numero.as_tuple())
print(numero.to_integral())
print(numero.compare(numero))
print(numero.compare_signal(numero))
