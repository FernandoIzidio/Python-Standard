from math import ceil
valor = float(input())
if valor >= 0:
    valor = ceil(valor)

intervalos = [range(0,25), range(25, 50), range(50, 75), range(75, 100)]

interuser = []
if any(valor in range(((inter.start+1) if inter.start > 0 else inter.start), inter.stop+1) and (interuser.append(inter) or True) for inter in intervalos):
    temp = str(interuser[-1]).split('range')
    if interuser[-1] != intervalos[0]:
        temp = ''.join(temp).split(')')
        intervalo = ']'.join(temp).split(', ')
        intervalo = ','.join(intervalo)
        print(f'Intervalo {intervalo}')
    else:
        temp = ''.join(temp).split(')')
        temp = ']'.join(temp).split('(')
        temp = '['.join(temp).split(', ')
        temp = ','.join(temp)
        print(f'Intervalo {temp}')
else:
    print('Fora de intervalo')