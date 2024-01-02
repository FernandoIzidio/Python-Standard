"""
Princípio da programação que se baseia em sempre que for possivel, tentar remover condicionais aninhadas

listas são valores/tipos mutaveis, e portanto não precisam de retorno ao entrar em uma função, pois a modificação já é salva
"""
from os import system
from time import sleep

tarefas = []
refazer = []

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refaz(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()

def limpar():
    system('clear')

while True:
    print('')
    print('Comandos: Listar, Desfazer, Refazer, Limpar, Sair.')
    cmd = input('Digite um comando ou tarefa:').capitalize()

    #Só vai chamar as funções listar, desfazer e etc, se a função lambda for chamada, a chamada é feita atravez de get, pega o valor da chave e retorna o valor da chave
    comandos = {
        'Listar': lambda: listar(tarefas),
        'Desfazer': lambda: desfazer(tarefas, refazer),
        'Refazer': lambda: refaz(tarefas, refazer),
        'Limpar': lambda: limpar(),
        'Adicionar': lambda: adicionar(cmd, tarefas)
    }
    
    if cmd != 'Sair':
        comando = comandos.get(cmd)() if comandos.get(cmd) != None else comandos['Adicionar']() 
    else:
        system('clear')
        print('Encerrando...')
        sleep(1)
        system('clear')
        break

   