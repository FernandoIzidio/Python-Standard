from os import system
from time import sleep



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

acertos = 0
for dicionario in perguntas:
    while True:
        print('='*50)
        print(dicionario['Pergunta'])
        print('-'*50)
        opt = iter(['A', 'B', 'C', 'D'])
        for item in dicionario['Opções']:
            print(f'{next(opt)}) {item}.')
        print('-'*50)
        esc = input('Digite a resposta:')
        if esc in dicionario['Opções']:
            if esc == dicionario['Resposta']:
                acertos += 1
            break
        system('cls')
        print('Erro: Digite uma resposta válida')
        sleep(2)
        system('cls')
    system('cls')

system('cls')
print('='*50)
print('PARABÉNS!!! Você gabaritou a prova!!!!' if acertos == 3 else 'MUITO BEM!!! Você acertou 2 de 3 questões.' if acertos == 2 else
'Boa sorte na próxima, você acertou 1 de 3 questões.' if acertos == 1 else 'A prática leva a perfeição, se esforce mais na próxima, você não acertou nenhum questão.')
print('='*50)