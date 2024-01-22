
#os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
from itertools import count
from os import walk, path, unlink
waydir = path.join(path.abspath('.'),'pacote_os', 'exemplo')
print(waydir)
print(path.exists(waydir))



contador = count()
for currentdir, subdirectorys, currentfiles in walk(waydir):
    contadoro = next(contador)
    print(f'{contadoro+1} Pasta Atual: {currentdir}')
    print(*subdirectorys, sep='\n')
    for file_ in currentfiles:
        wayfile = path.join(waydir, f'Pasta_{contadoro+1}', file_)
        print('')
        print(f'Nome do arquivo: {file_}')
        print(f'Caminho do arquivo: {wayfile}')
        unlink(wayfile)
        print(f'Removido com sucesso')