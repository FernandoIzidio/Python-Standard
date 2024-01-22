"""
os:
    path.expanduser('~') - Retorna o caminho até a pasta do usuário atual
    unlink - Remove pasta vazia, ou arquivo
    rename - Renomeia arquivo / Move arquivo
shutil:
    copy(caminho/file, caminhodestino/file) -> Copia um arquivo de um diretório para o outro
    copytree(caminho, caminhodestino) -> Copia todos os subdiretorios e arquivos de um caminho, e copia para outro caminho
    rmtree(caminho, ignore_errors=True) -> Remove todos o diretório e todos os seus subdiretórios e arquivos - Util para apagar diretórios com conteúdo
    move -> Renomeia arquivo, Move arquivo, possui menos erros que os.rename
"""

import os
import shutil
from os import system

HOME = os.path.expanduser('~')
DIRECTORY = os.path.join(HOME, 'Pasta_Teste')
print(*os.listdir(HOME), sep='\n')

os.makedirs(DIRECTORY , exist_ok=True)#Exist_ok é um parametro que suprime o erro fileexisterror, ou seja ele trata o erro e suprime o erro caso a pasta já exista

currentdirectory = os.path.join(os.path.abspath('.'), 'pacote_os', 'exemplo')


if os.path.exists(currentdirectory):
    for currentdir, subdirectorys, files in os.walk(currentdirectory):
        system('clear')
        os.makedirs(currentdirectory.replace('exemplo', 'exemplo2'), exist_ok=True)
        if files:
            for file in files:
                shutil.copy(os.path.join(currentdir, file), os.path.join(currentdirectory.replace('exemplo', 'exemplo2'), file))
