from time import sleep
from os import system

def guia():
    tt = '[1] Digite uma linha e pressione enter para confirmar a linha'
    print('='*len(tt))
    print(f'{"Guia de Uso":>35}')
    print('-'*len(tt))
    print(tt)
    print('[2] Digite "del" para apagar linha anterior')
    print('[3] Digite "undel" para refazer linha anterior')
    print('[4] Digite "\\n" para fazer quebra de linha')
    print('[5] Digite "Q!" para sair sem salvar')
    print('[6] Digite "WQ!" para sair e salvar o texto em arquivo txt')
    print('[7] Digite "help" para obter ajuda')
    print('[8] Digite "clear" para apagar o texto')
    print('-'*len(tt))
    input('Pressione qualquer tecla para iniciar o programa: ')
    print('-'*len(tt))
    sleep(1)
    system('clear')

def printao(texto):
    print('='*len(texto))
    print(texto)
    print('='*len(texto))