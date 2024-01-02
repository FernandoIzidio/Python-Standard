
"""
Tipo flexivel de representação de números, permite maior precisão na hora de representar números, é um tipo util para números que não exigem precisão grande.

metódos uteis:
    - obj.as_integer_ratio() - Retorna a fração mais próxima de representar o número
    - obj.is_integer() - Retorna true se o número flutuante, for um inteiro
    - obj.real - Parte real do número
    - obj.imag - Parte imaginária do número
    - obj.hex()- Retorna uma representação hexadecimal de um número flutuante
    - obj.fromhex(hexstr) - Converte um número hexadecimal em um número de ponto flutuante
"""

numero = float(75.54)
print(numero.as_integer_ratio())
print(numero.as_integer_ratio()[0] / numero.as_integer_ratio()[1])
hexa = numero.hex()
print(hexa)
print(numero.is_integer())
print(numero.fromhex(hexa))

