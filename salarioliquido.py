from os import system
from time import sleep

def calcularinss(salario: float)-> float:
    TAXA = {(0, 1320): 0.075 , (1320, 2571.29): 0.09, (2571.29, 3856.94): 0.12, (3856.94, float('inf')): 0.14}
    imposto = 0
    for faixa1, faixa2 in TAXA.keys():
        if faixa1 < salario <= faixa2:
            percent = TAXA.get((faixa1, faixa2))
            imposto += (salario - faixa1) * percent
        elif salario > faixa2:
            percent = TAXA.get((faixa1, faixa2))
            imposto += (faixa2 - faixa1) * percent
    return imposto

def calcularir(salario: float)-> float:
    TAXA = {(0, 2000): 0 , (2000, 3000): 0.08, (3000, 4500): 0.18, (4500, float('inf')): 0.28}
    imposto = 0
    for faixa1, faixa2 in TAXA.keys():
        if faixa1 < salario <= faixa2:
            percent = TAXA.get((faixa1, faixa2))
            imposto += (salario - faixa1) * percent
        elif salario > faixa2:
            percent = TAXA.get((faixa1, faixa2))
            imposto += (faixa2 - faixa1) * percent
    return imposto

def consulta_ir():
    system('clear')
    salario = float(input('Informe o seu sálario: '))
    print("Isento de IR." if salario == 0 else f"IR: R${calcularir(salario):.2f}".replace('.', ','))
    print('='*50)
    sleep(1.5)

def consulta_inss():
    system('clear')
    salario = float(input('Informe o seu sálario: '))
    print("Isento de INSS." if salario == 0 else f"INSS: R${calcularinss(salario):.2f}".replace('.',','))
    print('='*50)
    sleep(1.5)

def consulta_liquido():
    system('clear')
    salario = float(input('Informe o seu sálario: '))
    salario = (salario - calcularinss(salario)) 
    print(f"Sálario Líquido: {(salario - calcularir(salario)):.2f}".replace('.', ','))
    print('='*50)
    sleep(1.5)

while True:
    system('clear')
    print('='*110)
    print(f'{"Central do Calculo":^110}')
    print('='*110)
    print('[1] Consultar IR')
    print('[2] Consultar INSS')
    print('[3] Consultar Salário Líquido')
    print('[4] Sair')
    print('='*110)
    cmduser = input(":")

    comandos = {'1': lambda: consulta_ir(),
                '2': lambda: consulta_inss(),
                '3': lambda: consulta_liquido()}
        
    if comandos.get(cmduser):
        comandos.get(cmduser)()
    elif cmduser == '4':
        system('clear')
        print('Encerrando...')
        break