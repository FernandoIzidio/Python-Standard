from os import system
from time import sleep
listadetarefas = []
lixeira = []

def Listar(lista: list) -> None:
    if lista:
        system('clear')
        print('='*50)
        print('Tarefas: ')
        for pos, item in enumerate(lista):
            print(f'{pos+1:>4} - {item}')
        print(f'{"-"*50}')
        sleep(1.7)
    else:
        print('Nada a listar')
        sleep(1)

def Atualizar(lista:list, lista2:list, listavisual:list, msgdeerro: str) -> None:
    if lista:
        Listar(listavisual)
        while True:
            try:
                esc = int(input('Selecione um item: '))
            except (ValueError, TypeError):
                print('ERRO: Digite apenas números')
            else: 
                break
        try:
            lista2.append(lista[esc - 1])
            lista.pop((esc - 1))
        except IndexError:
            print('ERRO: Digitou posição invalida')
            sleep(1)
            
    else: 
        print(msgdeerro)
        sleep(1)

def Adicionar() -> None:
    global listadetarefas
    system('clear')
    listadetarefas.append(input('Digite uma tarefa:').capitalize())
    print(f'{"-"*50}\nTarefa adicionada a lista de tarefas com sucesso')
    sleep(1.3)

while True:
    system('clear')
    print('='*50)
    print('[1] - Listar')
    print('[2] - Adicionar')
    print('[3] - Desfazer')
    print('[4] - Refazer') 
    print('[5] - Sair')
    print('-'*50)
    cmd = input(':')

    if cmd == '5':
        break
    

    comandos = {'1': lambda: Listar(listadetarefas),
                '2': lambda: Adicionar(),
                '3': lambda: Atualizar(listadetarefas, lixeira, listadetarefas, 'Nada a Desfazer'),
                '4': lambda: Atualizar(lixeira, listadetarefas, lixeira, 'Nada a Refazer')}
     
    if comandos.get(cmd) != None:
        comandos.get(cmd)()