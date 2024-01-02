"""
Singleton: Objeto que só pode ser instanciado uma única vez no código

Váriveis livres: Disponiveis em todos os escopos de uma função

Non local varlivre
-Permite modificar o valor de uma variavel livre independente do escopo da função
-Resumindo o Nonlocal basicamente, permite que uma variável livre em uma função, tenha seu valor alterado, independente do escopo da função
-Faz com que a variavel livre, guarde seu valor na memória, e mantenha esse valor até o programa encerrar a sua execucação

-----------------------------------------------------------------------------------

"variável livre" se refere a uma variável que está definida em um escopo externo e é referenciada em um escopo interno


A palavra-chave nonlocal é usada para indicar que uma variável definida em um escopo externo ao escopo atual da função está sendo modificada dentro da função interna. Em outras palavras, quando você usa nonlocal, está sinalizando que a variável pertence a um escopo superior, não ao escopo local da função interna.




"""

def varlivre(msg:str):
    def interna(arg:str) -> str:
        return msg
    return interna


def concatenar(textoinicial:str):
    text = textoinicial
    def interna(textoaconcatenar:str)-> str:
        nonlocal text
        text = text + textoaconcatenar
        return text
    return interna


obj = varlivre('Texto1')
print(obj('+ Texto 2'))
print(obj('+ Texto 3'))
print('')

obj2 = concatenar('Texto1')
print(obj2('+ texto 2'))
print(obj2('+ texto 3'))
print(obj2('+ texto 4'))
    

def somador(initial: int):
    value = initial
    def interna(num:int):
        nonlocal value
        value += num
        return value
    return interna


somanumero = somador(0)
print(somanumero(5))
print(somanumero(8))
print(somanumero(7))
print(somanumero(5))
print(somanumero(3))
print(somanumero(5))
print(somanumero(8))
print(somanumero(7))
print(somanumero(5))
print(somanumero(3))

