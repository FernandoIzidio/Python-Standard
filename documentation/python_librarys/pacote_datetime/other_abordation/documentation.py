"""
Datetime melhor módulo para manipulação de datas

Funções e metódos uteis:
    obj = datetime(year, month, day) - Cria um objeto datetime
    obj = datetime(year, month, day, hours, minutes, seconds) - Cria um objeto datetime
    strftime(formatostr) -> str - Formata um objeto datetime para um formato especifico
    strptime(horastr, formatostr) -> objeto datetime- Cria um objeto datetime a partir de uma horastr e a partir de um formatostr
    obj = datetime.now() - Retorna o horário atual
    timestamp() - Retorna o número de segundos de 1970 até agora 
    datime.fromtimestamp(seconds) - Cria um objeto datetime, a partir dos segundos timestamp


Para mudar o timezone é preciso criar um objeto timezone, para criar um objeto timezone é usado o módulo pytz

Listas de timezones validas: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones - Esse artigo ajuda na criação de um objeto timezone validos

Operadores Relacionais:
    datetime > datetime ou datetime >= datetime - É possivel verificar qual data é maior, ou maior ou igual
    datetime < datetime ou datetime <= datetime - Qual data é menor, ou menor ou igual
    datetime != datetime - Qual data é diferente
    datetime == datetime - Qual data é igual

Operadores Aritméticos(Retornam objetos timedelta):
    timedelta = datetime - datetime2 - Retorna objeto time delta

Operações entre datetime e timedelta:
    datetime + timedelta - Aumenta o número de dias de uma data
    
Metódos de objetos timedelta:
    days - Retorna os dias de diferença de um objeto timedleta
    seconds - Retorna os segundos de diferença de um objeto timedelta
    microsseconds - Retorna os microsegundos de um objeto timedelta
    totalseconds() - Retorna o número total da diferença do obj timedelta em segundos


Objetos Time Delta:
    obj = timedelta(days, hours, minutes, seconds, microseconds)


Dateutil relativedelta - É uma extensão dos objetos time delta
Relative delta é possivel trabalhar com anos, meses, dias, e muito mais unidades de medidas


relativedelta(datafim, datainicio) - Retorna um timedelta/relativedelta com a diferença entre as duas datas
"""

from datetime import datetime, timedelta
from pytz import timezone
from dateutil import relativedelta
data=  datetime(2023, 8, 16, 16, 54, 3)
print(data)
datastr = "08/09/2023 08:06:23"
formatostr = "%d/%m/%Y %H:%M:%S"
hoursperson = datetime.strptime(datastr, formatostr)
print(hoursperson)
hourformated = hoursperson.strftime(formatostr)

print(hourformated)
print(datetime.now().strftime(formatostr))

print(datetime.now(timezone("Asia/Tokyo")).strftime(formatostr))

print(data > hoursperson)
delta = hoursperson - data
print(delta.days, delta.microseconds, delta.seconds)
print(delta.total_seconds())

untilnow = datetime.now().timestamp()
print(untilnow)
print(datetime.fromtimestamp(untilnow).strftime(formatostr))
dias = timedelta(10)
print('Evento daqui a 10 dias é na data: ', (datetime.now() + dias).strftime(formatostr))
