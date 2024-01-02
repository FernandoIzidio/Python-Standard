"""
Diretório de trabalho padrão é o mais alto nivel da pasta venv

Biblioteca muito util para interação com sistema operacional

abspath - retorna caminho absoluto PARA o diretório atual

__file__ - Retorna caminho absoluto DO módulo atual

bibliotecas:
   path

str.encode(encode:str) - Codifica uma string para uma codificação em especifico
   
ascii(str) -> str - Remove todos os caracters que não estão na codificação ascii, e retorna uma string na codificação ascii

b"" - Converte uma sequencia de caracters(string) em bytes. Nota: Todos os caracteres da string precisam estar na codificação ASCII para serem convertidos para bytes

chr(int)->str - Retorna um caracter baseado no seu identificador unicode

Metadados - É documentação de uma extrutura de dados, fornece informações da data de criação, modificação, tamanho, tipo, caracteristica dos conteudos do arquivo, extruturua, acesso, relações, ou seja metadados é documentação que informa tudo sobre uma extrutura de dados

Filedescriptor - Número inteiro equivalente ao processo em aberto do arquivo. todo arquivo aberto possui um filedescriptor para identificar o processo do arquivo em aberto
Path - Caminho absoluto de arquivo em formato str
paths relatives - Caminho relativo em string 
   
ReadableBuffer - Objeto que pode ser lido como uma sequência de bytes, ou arquivo aberto no formato leitura


Todos arquivos são salvos, criados por padrão no diretório de trabalho padrão

implemente funções que variam de acordo com o sistema, uma função clear que vai limpar de o terminal de acordo com o SO


Mascaras de Permissão ou Mode:
   São permissões que determinado processo tem no sistema operacional

   511 - Mascara de permissão mais permissiva de todas, da permissão total, a criação, exclusão, leitura, escrita, e execução.


leitura + escrita + execução   
5 + 1 + 1 = 7
7 é o nivel mais alto permissivo

mascaras de permissão octal:
   os.O_RDONLY - Concede apenas permissão de leitura a determinado processo.
   os.O_WRONLY - Concede apenas permissão de escrita a determinado processo
   os.O_RDWR - Concede permissão de leitura e escrita a um arquivo
   os.O_CREATE - Concede permissão de criar arquivo se ele não existir
   os.O_APPEND - Concede permissão de sempre escrever ao final do arquivo
   os.O_TRUNC - Trunca o arquivo, apaga o conteúdo de um arquivo se ele existir



os:

   os.makedirs(caminho:int, maskoct:int = 511, suprimeerror:bool = False) - Cria diretórios de forma segura e pode suprimir erros
   

   listdir(caminho:str) - Retorna uma lista com nomes dos subdiretorios e arquivos de um caminho. [subdirs e files do walk(porém de forma recursiva, entrando em cada subdir e subdir que surgir)]

   os.stat(caminho) -> objeto stat-  Retorna um objeto stat, que contem atributos para saber data de moficação de arquivo, tipo do arquivo, tamanho do arquivo, ou seja retorna um objeto com status/perfil completo do arquivo

   os.rename(old, new) - Move/renomeia diretório/arquivo

   fsencode(caminho:str)-> bytes - Codifica string(caminho arquivo) para codificação do sistema de arquivos atual

   fsdecode(caminho:bytes) -> str - Decodifica o caminhobytes para um versão str
   
   obj = fspath(caminhostrorbytes) - Garante que o caminho/arquivo esteja uma codificação/formato compativel com o sistema de arquivos


"""
import os
from pathlib import Path
currentdir = Path(__file__).parent



print(os.getcwd())
os.chdir(currentdir.__str__())
os.makedirs('PastaDeTrabalho', os.O_CREAT, True)
print(os.getcwd())

filedescriptor = os.open(currentdir / 'texto.txt', os.O_RDONLY)
print(filedescriptor)
filedescriptor2 = os.open(currentdir / "texto.txt", os.O_RDWR)
print(filedescriptor2)
os.write(filedescriptor2, os.fsencode("FLAMENGO É PIADA"))
dados = [b'', '']
while True:
   try:
      letra = os.read(filedescriptor, 1)
      dados[0] += letra
      dados[1] += letra.decode('utf-8')

      print(letra.decode('utf-8'))
   except:
      print(F'Erro ao decodificar carecter {letra} na codificação UTF-8')

   if not letra:
      break

os.close(filedescriptor)
os.close(filedescriptor2)

print(os.fspath(currentdir.__str__()))


print(os.fsdecode(os.fsencode("FLAMENGO É PIADA")))
print(os.fsdecode(dados[0]))
print(dados[1])