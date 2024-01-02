from math import floor
med = []
while True:
    x = float(input())
    if 0 <= x <= 10:
        med.append(x)
        if len(med) == 2:
            print(f'media = {(sum(med))/2:.2f}')
            break
    else:
        print('nota invalida')