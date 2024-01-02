from os import system
from time import sleep

lanches = {'1': ['Cachorro Quente', 4], '2':['X-Salada',4.50], '3': ['X-Bacon',5], '4': ['Torrada Simples', 2], '5': ['Refrigerante', 1.50]}
while True:
    system('clear')
    print('='*50)
    print(f'{"Lanchonete":^50}')
    print('='*50)
    for cod, conteudo in lanches.items():
        print(f'|  {cod} {"":>10}{conteudo[0]:<16}{f"R$ {conteudo[-1]:.2f}":>16}  |'.replace('.',','))
    print('='*50)
    opt = input(':')
    print('-'*50)
    if lanches.get(opt):
        int(input('Informe a quantidade de items:'))
        break
    print('ERRO: Digite uma opção válida')
    sleep(1.6)

