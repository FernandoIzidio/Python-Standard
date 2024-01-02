"""
Nova extrutura condicional do python que surgiu na versão 3.10, e tem como extrutura basica:

match variavel:

    case n:
    ...

    caso nenhuma das condições seja true, execute essa bloco de códigos
    case _:
    
Na pratica não muda muita coisa em processamento, mas é uma extrutura muito util, e que ajuda bastante para melhorar a sintaxe e legibilidade

Vale ressaltar que o guardclause determina ser uma má pratica extruturas aninhadas muito extensas

"""
from os import system 
from time import sleep


while True:
    try:
        x = int(input('Digite o dia da semana(número inteiro):'))
    except (ValueError, TypeError):
        print('Erro: Digite apenas números inteiros.')
        sleep(2)
        system('cls')
    else:
        if x in range(1,8):
            break
        else:
            print('Erro: Digite um número válido.')
            sleep(2)
            system('cls')

match x:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda-Feira')
    case 3:
        print('Terça-Feira')
    case 4:
        print('Quarta-Feira')
    case 5:
        print('Quinta-Feira')
    case 6:
        print('Sexta-Feira')
    case 7:
        print('Sábado')