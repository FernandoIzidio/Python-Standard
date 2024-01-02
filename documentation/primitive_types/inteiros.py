"""
Tipo mais primitivo do python, usado para fazer operações muitas operações númericas

bin(numero) - Representação de um número em binário
Principais metódos:
    - real - parte real do número
    - imag - parte imaginária do número
    - num.bit_lenght() - int - Retorna o número de bits(0 e 1) necessários para representar o números
    - as_integer_ratio() - tuple - Retorna a fração mais próxima de representar o número
    - int().from_bytes(byterepresentation, byteorder=[little or big]) - Converte uma ou mais sequências de bytes, em um número inteiro
    - to_bytes(numberofbytes, byteorder) - Converte um número decimal, em uma ou mais sequências de bytes de um byteorder
    - bit_count() int - Retorna o número de bits true(1) em uma representação binária
    - numero.conjugate() - troca o sinal apenas da parte imaginária do número exemplo 4 + 3j vira 4 - 3j
    
    >> - deslocamento a direita, acrescenta um 0 a direita da representação binária, e divide por 2 a representação decimal
    << - Deslocamento a esquerda, acrescenta um 0 a esquerda da representação binária, e multiplica por 2

 o operador bit a bit, retorna 1 se os bits forem diferentes, e 0 se os bits forem iguais
0 ^ 0 resulta em 0 (0 é igual a 0).
0 ^ 1 resulta em 1 (0 é diferente de 1).
1 ^ 0 resulta em 1 (1 é diferente de 0).
1 ^ 1 resulta em 0 (1 é igual a 1).
    
    """

NUMERO = int(100)

print(~NUMERO)
print(bin(NUMERO))
print(NUMERO.as_integer_ratio())
print('Números de bits 1: ', NUMERO.bit_count())
bits = NUMERO.to_bytes(2, 'big')
print(bits)
print(int().from_bytes(bits, 'big'))
