

"""
Context Manager:
    __init__(self, mode, wayfile) - Recebe caminho de modo de abertura de arquivo

    __enter__(self) - Deve abrir o arquivo e retornar o conteudo do arquivo

    __exit__(self, classerror, objerro, traceback) - Deve fechar o arquivo e tratar a exceção se ocorrer.
    se retornar true, suprime um erro.


todo conteúdo é salvo no inicio do diretorio pai/ ou seja no inicio do venv 
"""
from pathlib import Path

currentdir = Path(__file__).parent

class MyPersonOpen:
    def __init__(self, wayfile, openmode) -> None:
        self.openmode = openmode
        self.way = wayfile


    def __enter__(self):
        self.content = open(self.way, self.openmode)
        return self.content
    
    def __exit__(self, classerror, objerro, traceback):
        self.content.close()
        return True #Suprime erro se ocorrer
    

with MyPersonOpen(currentdir / 'texto.txt', 'w') as textfile:
    textfile.writelines(['My person context manager\n', 'Testing methods', 'Okay HELLLLOOOOOOO'])