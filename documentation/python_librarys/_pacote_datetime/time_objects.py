"""
Time é uma classe excelente quando se precisa fazer manipulação de horários.

time(hours, minutes, seconds, microseconds) - Argumentos necessários para criação de um objeto time

Metódos uteis:
    dst - Retorna o deslocamento utc de um objeto time no summer time(horário de verão), retorna 0 se não tiver horário de verão

    fold - Número da ocorrência do horário no dia, 0 primeira ocorrência do horário no dia, 1 segunda ocorrência do horário no mesmo dia

    utcoffset - Retorna o deslocamento utc(timedelta) do objeto time

    tzname -  Retorna o nome descritivo da timezone

    isoformat - Retorna a representação do objeto time, no formato ISO

    replace(hours, minutes, seconds, microseconds)  - Altera os valores de um objeto time

    fromisoformat(AAAA-MM-DD:str) - Cria um objeto time, a partir do formato iso

    strftime(format:str) - Formata um objeto time para determinado formato

"""

from datetime import time, timezone, datetime


universaltime = datetime.now(timezone.utc).time()
universaltime = time(universaltime.hour, universaltime.minute, universaltime.second, universaltime.microsecond, timezone.utc, fold=0)
brformat = "%H:%M:%S"

print(universaltime.isoformat())
print(universaltime.fold)
print(universaltime.dst())
print(universaltime.utcoffset())
print(universaltime.tzname())
print(universaltime.strftime(brformat))
print(time.fromisoformat("06:58:36"), type(time.fromisoformat("06:58:36")))