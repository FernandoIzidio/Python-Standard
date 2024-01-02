"""
sys.argv - Mostra argumentos do script/módulo
O primeiro argumento sempre é o nome do módulo
python3 __name__.py value value

argparse - É um argv mais robusto, ou seja argumentos de script de forma mais robusta.
argparse recebe uma chave de argumento e o valor do argumento ex:
python3 __name__.py arg1 value arg2 value
"""
from sys import argv

argumentos = argv
qtd = len(argumentos)
print(argumentos)

if argv == 1:
    print('Você não passou nenhum argumento pro script')
else:
    for pos, arg in enumerate(argumentos):
        print(f'Argumento número {pos+1} : {arg}')