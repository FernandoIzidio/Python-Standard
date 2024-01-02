from time import sleep
from os import system
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acer = 0

for dicionario in perguntas:
    opt = ['A)', 'B)', 'C)', 'D)']
    opt = iter(opt)
    print(dicionario['Pergunta'])
    for option in dicionario['Opções']:
        print(f'{next(opt)} {option}')
    res = input(':')
    if res ==  dicionario['Resposta']:
        acer += 1
    sleep(1)
    system('cls')

sleep(2)
system('cls')
print('Parabéns você gabaritou a prova' if acer == 3 else 'Você foi muito bem, acertou 2 de 3 questões' if acer == 2 else f'Boa sorte na próxima, acertou {acer} de 3 questões.')


