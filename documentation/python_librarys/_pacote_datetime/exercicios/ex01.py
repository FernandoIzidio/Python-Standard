from datetime import datetime, timedelta, timezone
from dateutil import relativedelta
import calendar

print('='*50)
print(f'{"Central do tempo":^50}')
print('-'*50)
print('[1] - Consultar hora atual')
print('[2] - Abrir calendário')
print('[3] - Calcular prazos')
print('[4] - Verificar dias')

timezone()

from datetime import datetime, timedelta
entrada = input().split()
horarioinicio = datetime.strptime(f'{entrada[0]}','%H')
horariofim = datetime.strptime(f'{entrada[1]}','%H')
if horarioinicio > horariofim:
    horariofim = horariofim + timedelta(days=1)
duracao = timedelta(days=1) - (horarioinicio - horariofim)

horas = (duracao).seconds // 3600
minutos = ((duracao).seconds % 3600) // 60

print(f'O JOGO DUROU {horas} HORA(S)' if not(horas == 0) else f'O JOGO DUROU 24 HORA(S)')