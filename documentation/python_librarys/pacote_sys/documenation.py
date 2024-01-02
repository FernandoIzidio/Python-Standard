
"""
sys é o melhor modulo para interagir com o interpretador, execução de módulos, argumentos para script python, e configurações de ambiente python

sys.argv - Retorna os argumentos passados na execução de um script, o primeiro argumento sempre vai ser caminho/nome do módulo.


"""
import sys
print(f'{len(sys.argv)} Argumentos passados: ')
print(*sys.argv, sep='\n')


print('')

cmds = {'a': 'Abacaxi', 'b': 'Bola', 'c': 'Carro', 'd': 'Dado', 'e': 'Escola', 'f': 'Faca', 'g': 'Goiaba', 'h': "Hello World!!!", 'i': 'Indio', 'j': 'Jabuticaba', 'k':'Karol', 'l': 'Lápis', 'm': 'Melão', 'n': 'Navio', 'o': 'Outono', 'p': 'Pato', 'q': 'Queijo', 'r': 'Rato', 's': 'Sapo', 't':'Tatu', 'u': 'Ultra', 'v': 'Viola', 'w': 'Willian', 'x': 'Xadrez', 'y': 'Yoyo', 'Z': 'Zebra'}


for arg in sys.argv:
    if cmds.get(arg):
        print(cmds.get(arg))