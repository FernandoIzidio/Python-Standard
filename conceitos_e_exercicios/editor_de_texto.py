from time import sleep
from os import system
from guia import guia, printao
from copy import deepcopy
#Funções gráficas acima

def digitar_e_apagar_texto(texto:str):
    acumulador = texto
    def interna(newtext: str, condition:bool)->str:
        nonlocal acumulador
        if condition:
            acumulador += newtext 
            return acumulador
        acumulador = acumulador.replace(newtext, '')
        return acumulador
    return interna

def showtext(texto):
    for linha in texto:
        if linha != '\\n':
            print(linha, end='')
        else:
            print('')


ctrlz = []
insert_line = digitar_e_apagar_texto('')

#Verifica opção por arquivo existente ou não
while True:
    esc = input('Deseja Editar arquivo txt existente[S/N]:').upper()
    
    if esc in ('S', 'N'):
        if esc == 'S':
            while True:
                
                filename = input('Digite o nome do arquivo(digite q! para cancelar): ')
                
                if filename != "q!":
                    try:
                        with open(f'{filename}.txt', 'r', encoding='utf8') as arquivotexto:
                            textfile = arquivotexto.readlines()
                            break
                    except (FileExistsError, FileNotFoundError):
                        system('clear')
                        printao('ERRO: Arquivo não encontrado, tente novamente.')
                        sleep(1)
                        system('clear')
                else:
                    esc = 'N'
                    break
        break

    system('clear')
    printao('ERRO: Digite uma opção válida')
    sleep(1)
    system('clear')

#Carrega os dados do arquivo existente, ou começa do zero
hasprefile = (esc == 'S')
if hasprefile:
    textcheck = textfile
    for linha in textfile:
        insert_line(linha, True)
else:
    textcheck = []

system('clear')
guia()
while True:
    system('clear')
    showtext(textcheck)
    print()
    print('-'*114)
    linha = input(':')
    match linha:
        case 'del':
            #Verifica se tem alguma linha em textcheck
            if textcheck:
                ctrlz.append(textcheck[-1])
                insert_line(textcheck[-1], False)
                textcheck.pop()
            else:
                print('Não digitou nada ainda')
                sleep(1)
        case 'undel':
            #Verifica se tem alguma linha em ControlZ
            if ctrlz:
                if all(isinstance(item, str) for item in ctrlz):
                    textcheck.append(ctrlz[-1])
                    insert_line(ctrlz[-1], True)
                    ctrlz.pop()
                else:
                    for item in ctrlz:
                        if isinstance(item, list):
                            for string in item:
                                textcheck.append(string)
                                insert_line(string, True)
                            ctrlz.remove(item)
            else:
                print('Nada a desfazer.')
                sleep(1)        
        case '\\n':
            insert_line('\n', True)
            textcheck.append('\\n')
        case "Q!":
            system('clear')
            printao('Encerrando...')
            sleep(1)
            system('clear')
            break
        case "WQ!":
            #Senha para o insert_line não remover nenhuma linha do texto, e para o conteúdo do insert line ser armazenado em data
            passwd = 'INVALIDSTRING418A3@687423#@@!!!34829@!@7711'
            data = insert_line(passwd, False)
        
            #Verifica se o usuário está editando um arquivo existente, ou se está criando um novo

            if hasprefile:
                textname = filename
            else:
                system('clear')
                textname = input('Digite o nome do arquivo:')

            with open(f'{textname}.txt', 'w', encoding='utf8') as arquivo:
                arquivo.write(data) 

            system('clear')
            printao('Encerrando...')
            sleep(1)
            system('clear')
            break
        case "help":
            system('clear')
            guia()
        case "clear":
            ctrlz.append(deepcopy(textcheck))
            textcheck.clear()
            insert_line = digitar_e_apagar_texto('')
        case _:
            textcheck.append(linha)
            insert_line(linha, True)
    