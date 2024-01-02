
"""
Tipo usado para expressar textos, é um iterable, e é muito fácil de manipular

Metódos uteis:
    capitalize - str Modifica primeira letra para maiusculo
    casefold -str - Converte string para minúsculo, e torna igual independente da codificação
    lower() - Transforma string em minúsculo
    upper() - Converte string para maiúsculo

    center(width, fillchar) ->str - Centraliza uma string, em uma largura especifica, pode ser centralizada por espaços em brancos(valor pradão fillchar), ou qualquer outro valor
    count(value) int - Mostra o número de vezes que um caracter se repetiu dentro da string
    index(value) int - Retorna a posição de um valor dentro da string, caso não encontre lança um ValueError
    find(value) int - Retorna a posição de um valor dentro da string, caso não encontre retorna -1
    startswith(value) -> bool - Verifica se string começa com um valor
    endswith(value) -> Bool - Verifica se string termina com um valor
    expandtabs(widthtab) str - Aumenta a largura, número de caracters de uma tabulação
    strip() - str - Remove espaços em branco a esquerda e direita
    title() - str - Funciona como capitalize, mas converte as primeiras letras para maiusculo, de todas as substrings separadas por espaço na string
    .format() - Funcina como as f-strings, ou operador %, é para colocar variaveis no texto
    .zfill(width) - Prenche a string com zeros(0) a esquerda, para atingir largura definida
    "SEP".join(iterable) - str - Une os itens de um iterable, seperando cada item pelo valor do seperador, no final retorna um string com os itens unidos
    str.split(sep) -list - Sepera todas as substrings de uma string de acordo com o valor do serpador, e retorna uma uma lista, onde cada substring é um item da listas
    str.encode(encoding) - Define a codificação de uma string
    swapcase() - str - Converte caracters minúsculo para maiúsuculos, e caracters maiúsculo para minúsculos
    replace(oldstring, newstring) - Troca todas as ocorrências de uma substring por um novo valor
    splitlines(keepwhitespaces=bool-false) -list- Converte uma string em uma lista, onde cada item dessa lista é separado por uma quebra de linha da string
    partition(sep) ->tuple - Uma string sera repartida em 3 partes de acordo com o separador, e retornara uma tupla com 3 items/partes da string
    isalnum - Verifica se uma string é alphanúmerica (adfsa7894)
    isalpha - Verifica se uma string é alfabetica (tem apenas letras)
    isdigit - Verifica se todos os caracters de um string são númericos de 0 a 9, no ASCII
    isdecimal - Verifica se todos os caracters de um string são númericos de 0 a 9, no ASCII
    isnumeric - Verifica se todos os caracters de uma string são númericos de 0 a 9, independente da codificação, pode ser romano, arabe e etc
    islower - Verifica se uma string está em MINÚSCULO
    isupper - Verifica se uma string está em maísculo
    isidentifier -  verifica se o conteúdo da string poderia ser usado como nome de variavel
    str.isascii() - Verifica se string está na codificação ASCII
    str.isprintible() - Verifica se uma string é printavel
    str.isspace() - Verifica se a string é um espaço em branco
    str.istitle() - Verifica se a string está na TitleCase, onde cada substring separada por espaço, começa com letra maiúscula
    
    """

texto = "Trú cO"
print(texto.casefold())
print(f'{texto:=^50}')
print(texto.center(100, '*'))
print(texto.index('ú'))
print(texto.endswith('cO'))
tabulacao = "\ttexto texto2"
print(tabulacao.expandtabs(20))
print(tabulacao.find('t', 2))
print(texto.title())
print(texto.zfill(20))
print(texto.startswith('T'))
print(tabulacao.split(' '))
lista= ['A','B','C']
print(''.join(lista))
print(tabulacao.encode())
print(texto.swapcase())
print(tabulacao.replace('texto', 'OLá'))
poesia = 'Feliz é aquele\nQue não tem medo de parecer ríduculo'
print(poesia.splitlines())
print(poesia.partition(' '))
print(poesia.isalnum())
myvar = 'var_45'
var2 = 'texto2'
print('Pode ser nome de variavel: ',myvar.isidentifier())
print('Pode ser nome de variavel: ',var2.isidentifier())
numbers = 'Ⅳ'
print(numbers.isdecimal())
print(numbers.isdigit())
print(numbers.isnumeric())
numbers.isascii()
numbers.isprintable()
numbers.isspace
numbers.istitle
numbers.rsplit