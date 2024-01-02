from os import system, remove
from time import sleep
from copy import deepcopy
from json import load, dump
while True:
    opt = input('Deseja usar um arquivo existente[S/N]:').upper()
    if opt in ('S', 'N'):
        if opt == 'S':
            while True:
                filename = input('Digite o nome do arquivo json(q! para desistir):')
                
                if filename != 'q!':
                    try:
                        with open(f'{filename}.json', 'r', encoding='utf8') as datafile:
                            data = load(datafile)
                    except (FileExistsError, FileNotFoundError):
                        system('clear')
                        print('ERRO: Arquivo não existe/não encontrado.')
                        sleep(1)
                        system('clear')
                    else:
                        break
                else:
                    opt = 'N'
                    break
        break
    system('clear')
    print('ERRO: Digite uma opção válida')
    sleep(1)
    system('clear')




if opt == 'S':
    tarefas = deepcopy(data)
    if filename != 'temp':
        saveble = True
    else:
        saveble = False
else:
    tarefas = []
    saveble = False

refazer = []



def listar(iterable):
    if iterable:
        print('')
        print('Tarefas:')
        for item in iterable:
            print(item)
    else:
        print('Nada a listar.')

def update(renaming: bool, Reset: bool=False):
    global filename, data
    if not Reset:
        if saveble or renaming:
            with open(f'{filename}.json', 'w', encoding='utf8') as fileupdate:
                dump(tarefas, fileupdate, ensure_ascii=False, indent=2)
        else:
            with open('temp.json', 'w', encoding='utf8') as filenew:
                dump(tarefas, filenew, ensure_ascii=False, indent=2)
    else:
        with open(f'{filename}.json', 'w', encoding='utf8') as fileupdate:
                dump(data, fileupdate, ensure_ascii=False, indent=2)

while True:
    print('')
    print("Comandos: Listar, Desfazer, Refazer, Sair(Sem Salvar), Salvar(Sair), Limpar.")
    cmd = input('Digite um comando ou tarefa:').capitalize()
    match cmd:
        case "Listar":
            listar(tarefas)
        case "Desfazer":
            if tarefas:
                refazer.append(tarefas[-1])
                tarefas.pop()
                update(False)
                listar(tarefas)
            else:
                print('Nada a desfazer.')
        case 'Refazer':
            if refazer:
                tarefas.append(refazer[-1])
                refazer.pop()
                update(False)
                listar(tarefas)
            else:
                print('Nada a refazer')
        case 'Limpar':
            system('clear')
        case 'Sair':
            if not saveble:
                remove('temp.json')
            else:
                update(False, True)

            system('clear')
            print('Encerrando...')
            sleep(1)
            system('clear')
            break
        case 'Salvar':
            if not saveble:
                filename = input('Digite o nome do arquivo para salvar:')
                update(True)
                remove('temp.json')

            system('clear')
            print('Encerrando...')
            sleep(1)
            system('clear')
            break
        case _:
            tarefas.append(cmd)
            update(False)
            listar(tarefas)
            

