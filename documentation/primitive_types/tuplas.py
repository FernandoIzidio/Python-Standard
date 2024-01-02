"""
Tipo de dados imutavel, após sua declaração não é possivel fazer alterações

Metódos uteis:
    tuple.count(value) -> int - Retorna quantas vezes um valor se repetiu em uma tupla
    tuple.index(value) -> int - Retorna a posição de um valor na tupla
    
    """

dados = tuple(item for lista in (['A','B','C', 'A'] for count in range(10)) for item in lista)
print(dados)
print(dados.count('A'))
print(dados.index('B'))
print(tuple([123, 487, [48, 78], {'truco', ''}]))