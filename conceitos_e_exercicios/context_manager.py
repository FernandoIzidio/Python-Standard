"""
Metódos importantes em manipulação de arquivos:
arquivo.read(size:int)->str:
-Lê todo o arquivo, e retorna todo o conteúdo como uma string
-Size: Define até que caractere vai ser lido o arquivo

arquivo.readlines(hint:int)->list:
-Lê todo o arquivo, retorna uma lista(str), onde cada item da lista é uma linha do arquivo
-Hint: Define até que caractere vai ser lido o arquivo

arquivo.readline(hint:int)->string:
-Funciona como a função next(iterator)
-Lê a primeira linha do arquivo e retorna o conteúdo da linha em string, ao ser chamado dnv retorna a próxima linha em string
-Hint: Define até que caractere vai ser lido o arquivo

arquivo.readable()->bool:
-Retorna um valor boolean que verifica se o arquivo é hábil para leitura

arquivo.writable()->bool:
-Retorna um valor boolean que verifica se o arquivo é hábil para escrita

arquivo.seekable()->bool:
-Retorna um valor boolean que verifica se o arquivo é hábil para movimentação de cursor

write(string): 
-Escreve uma string no arquivo. Se o arquivo já existir, o conteúdo anterior será substituído.

append(string): 
-Abre o arquivo no modo de anexação ('a') e permite adicionar conteúdo ao final do arquivo.
writelines(iterable): 
-Escreve uma lista de strings no arquivo, onde cada string é uma linha.

seek(offset, whence=0):
-offset: A posição para a qual você deseja mover o cursor no arquivo. É um número inteiro que representa o deslocamento em relação ao ponto de referência especificado.
whence: É um argumento opcional que define o ponto de referência para o deslocamento. -Os valores possíveis são 0 (início do arquivo), 1 (posição atual) e 2 (final do arquivo)

arquivo.close():
-Fecha o arquivo e salva as alterações


"""
from json import dump
from os import system

with open('predados.txt', 'r') as arquivo:
    dados = arquivo.readlines()
    print(dados)
    print('\\')
    input()
    system('clear')
    arquivo
    
    temp = []
    for string in dados:
        t = []
        for letra in string:
            if letra == "(" or letra == ")" or letra == "'":
                del letra
            else:
                t.append(letra)
        temp.append(''.join(t))
    
    temp = [string.split('\n') for string in temp]
    temp = [string for lista in temp for string in lista if string]
    temp = [string.split(',') for string in temp]

with open('dados.json', 'w', encoding='utf8') as data:
    dump(temp, data, ensure_ascii=False, indent=2) 
    