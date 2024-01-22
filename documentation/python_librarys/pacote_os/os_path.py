"""

sys.getsizeof retorna qual o tamanho de um objeto python

os.path.getsize - Retorna o tamanho em bytes de um arquivo/diretório

Módulo excelente para manipulação de caminhos

Ele pode ser substituido pela pathlib, porém tem muitos sistemas legados que utilizam versões inferiores a 3.4, que ainda usam o os.path para manipulação de arquivos.

Sistema Legado- Softwares grandes desenvolvido em versões antigas de linguagens, que carregam legado/importância até hoje

__file__ - Retorna caminho absoluto DO módulo atual

path:
    join(*strs:str) -> str : Recebe vários strs, e concatena todas, retornando um caminho de arquivo com essas strs

    split(caminho:str) -> diretorio:str, file:str -> Separa caminho do diretório de nome do  arquivo 

    splitext(caminho:str) -> caminho:str, extensãodoarquivo:str -> Separa extensão do caminho

    splitdrive(caminho:str) -> Separa o hd/disco, do caminho

    exists(caminho:str) -> bool -> Verifica se um caminho existe ou não

    abspath(caminho:str) -> str -> Retorna caminho absoluto PARA o diretório/arquivo especificado

    basename(caminho:str) -> str -> Retorna o ultimo arquivo/diretório de um caminho

    isdir(caminhoabs:str) -> bool -> Veriifica se determinado caminho é um diretório

    dirname(caminho:str) -> Retorna apenas o caminho do diretório, e remove a parte do arquivo

    expanduser('~') - Retorna o caminho para home

    path.getsize -  Retorna o tamanho em bytes de um arquivo/objeto

    path.normpath() - Normaliza um caminho, removendo barras duplas

    path.isfile() - Verifica se determinado caminho é um arquivo

    path.islink() - Verifica se é um atalho

    path.commonpreffix(listPath) - Retorna todo o caminho que uma lista de caminhos tem entre si, e retorna apenas um str, que representa todo o caminho em caminho comum da lista de diretórios

    path.realpath('.') - Semalhente ao resolve do js, realpath, vai tratar de caminhos relativos, e vai converter tudo para caminho absoluto

listdir('str') -> list[str] -> Retorna uma lista de strings, com os diretorios e arquivos de um caminho, resumindo, lista os diretórios e arquivos de um caminho em uma lista
rename
remove

"""
from os import path, system, listdir


print(path.realpath('.'))
caminho_ramdom = path.join('Desktop', 'Truco', 'Ladrao.txt')
print(caminho_ramdom)
diretorio, file = path.split(caminho_ramdom)
print(diretorio)
print(file)

caminho, extensao = path.splitext(caminho_ramdom)
print(caminho)
print(extensao)

print(path.exists(caminho_ramdom))

print(path.abspath('.'))
print(path.basename(f'./{__name__}'))
print(path.dirname(f'/home/pennpc/venv'))
print('')
print('')
print('Arquivos dos diretórios internos:')
print('')
wayabs = path.abspath('.')
for pasta in listdir(wayabs):
    if not path.isdir(path.join(wayabs, pasta)):
        continue
    print(pasta)
    print('')
    for file in listdir(pasta):
        print(file)


paths = ['/home/user/file1.txt', '/home/user/file2.txt']
common_prefix = path.commonprefix(paths)
print(common_prefix)