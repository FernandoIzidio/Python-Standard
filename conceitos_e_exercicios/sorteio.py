from os import system
from time import sleep
from random import randint

def menu() -> None:
    print('='*50)
    print(f'{"Central Lotérica":^50}')
    print('='*50)
    print(f'|{"[1] - Lotofácil":<48}|')
    print(f'|{"[2] - Megasena":<48}|')
    print(f'|{"[3] - Quina":<48}|')
    print(f'|{"[4] - Duplasena":<48}|')
    print(f'|{"[5] - Lotomania":<48}|')
    print(f'|{"[6] - Sair":<48}|')
    print('='*50)


def sortear(quant: int, limite: int) -> None:
    system('clear')
    print('='*50)
    jogos = int(input('Quantos jogos deseja sortear:'))
    print('='*50)
    sleep(1)
    system('clear')

    numeros = [[] for cont2 in range(jogos)]
            
    for jogo in numeros:
        while not len(jogo) == quant:
            numero = randint(1,limite)
            if numero not in jogo:
                jogo.append(numero)
        jogo.sort()
    
    print('='*50)
    print('Números sorteados.')
    print('-'*50)

    ind = 1
    for jogo in numeros:
        print(f'Jogo {ind}:')
        print('-'*50)
        for numero in jogo:
            print(f'{numero},' if numero != jogo[-1] else f'{numero}.', end='')
        print('')
        print('-'*50)
        ind += 1
    print('='*50)
    input('Next:')

while True:
    system('clear')
    menu()
    comandos = {'1': lambda : sortear(15, 25),
                '2': lambda : sortear(6, 60),
                '3': lambda : sortear(5, 80),
                '4': lambda : sortear(6, 50),
                '5': lambda : sortear(50, 100)}
    
    usercomand = input(':')

    if usercomand == 6:
        system('clear')
        print('='*50)
        print('Encerrando...')
        print('='*50)
        sleep(2)
        system('clear')
        break
            
    if comandos.get(usercomand) != None:
       comandos.get(usercomand)()
    
    print('ERRO: Seleciona uma opção válida')
