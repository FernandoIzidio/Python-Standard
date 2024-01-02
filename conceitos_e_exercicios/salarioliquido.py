from os import system
from time import sleep

def calcularinss(salario: float)-> float:
    imposto = 0
    if not(salario > 1320):
        imposto += (salario * 0.075)
    elif not (salario > 2571.29):
        imposto += (1320 * 0.075) + ((salario-1320) * 0.09)
    elif not (salario > 3856.94):
        imposto += (1320 * 0.075) + ((2571.29 - 1320) * 0.09) + ((salario - 2571.29) * 0.12)
    else:
        imposto += (1320 * 0.075) + ((2571.29 - 1320) * 0.09) + ((3856.95 -2571.29) * 0.12) + ((salario - 3856.95) * 0.14)
    return imposto

def calcularir(salario: float)-> float:
    imposto = 0
    if (salario < 2000):
        imposto = 0
    elif (salario < 3000):
        imposto += ((salario - 2000) * 0.08)
    elif (salario < 4500):
        imposto += ((3000 - 2000) * 0.08) + ((salario - 3000) * 0.18)
    else:
        imposto += ((3000 - 2000) * 0.08) + ((4500 - 3000) * 0.18) + ((salario - 4500) * 0.28)
    return imposto

def informasal():
    global checasalario, salario
    if not checasalario:
        while True:
            try:
                print('='*50)
                salario = float(input("Informe o seu sálario:"))
                print('-'*50)
            except:
                system('clear')
                print('ERRO: Digite apenas números')
                sleep(1)
                system('clear')
            else:
                checasalario = True
                break
    return salario

checasalario = False
while True:
    while True:
        try:
            system('clear')
            print('='*110)
            print(f'{"Central do Calculo":^110}')
            print('='*110)
            print('[1] Consultar IR')
            print('[2] Consultar INSS')
            print('[3] Consultar Salário Líquido')
            print('[4] Sair')
            print('='*110)
            opt = int(input(":"))
        except:
            system('clear')
            print("ERRO: Digite apenas números inteiros.")
            sleep(1)
            system('clear')
        else:
            break
    match opt:
        case 1:
            system('clear')
            informasal()
            print("Isento de IR." if salario == 0 else f"IR: R${calcularir(salario):.2f}".replace('.', ','))
            print('='*50)
            sleep(2)
        case 2:
            system('clear')
            informasal()
            print("Isento de INSS." if salario == 0 else f"INSS: R${calcularinss(salario):.2f}".replace('.',','))
            print('='*50)
            sleep(2)
        case 3:
            system('clear')
            informasal()
            salario = (salario - calcularinss(salario)) 
            print(f"Sálario Líquido: {(salario - calcularir(salario)):.2f}".replace('.', ','))
            print('='*50)
            sleep(2)
        case 4:
            system("clear")
            print('='*50)
            print("Encerrando...")
            print('='*50)
            sleep(1)
            break
        case _:
            system("clear")
            print("ERRO: Selecione uma opção válida")
            sleep(1)
            