"""
Para adicionar notas as exceções, é preciso instanciar a classe da exceção
e usar o metódo add_notes(msg) para adicionar nota ao objeto da exceção

__notes__ - atributo retorna lista com todas notas da exceção, cada nota é uma linha no erro

"""


class My_Exception(Exception):  
    ...

erro = My_Exception('ERRO')
try:
    raise erro
except My_Exception as error:
    print(error)
    print(error.args)