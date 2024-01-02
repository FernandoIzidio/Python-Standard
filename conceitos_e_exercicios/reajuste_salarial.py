salario = float(input())
reajustes = {(0, 400): 0.15,(400, 800): 0.12, (800, 1200): 0.10, (1200, 2000): 0.07, (2000, float('inf')): 0.04}

def get_reajuste(salario:float):
    global reajustes
    for chave, valor in reajustes.items():
        if  chave[0] < salario <= chave[1]:
            return valor
        
reajuste = get_reajuste(salario)
print(f'Novo salario: {salario + (salario * reajuste):.2f}')
print(f'Reajuste ganho: {salario * reajuste:.2f}')
print(f'Em percentual: {int(reajuste * 100)} %')