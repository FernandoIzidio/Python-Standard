"""
Time cria um objeto com atributos hora, minuto, segundo

Date cria um objeto com atributos ano, mês, e dia
metódos uteís
    obj.weekday() -> Retorna o dia da semana de uma data

timezone retorna o horário de uma determinada zona/país

timestamp() - Retorna quantos segundos tem uma data começando a contar a partir de 31/12/1969


delta = datafinal - datanicio
retorna a diferença entre as duas datas em dias

delta.days - Retorna em dias
delta.seconds - Retorna em segundos
delta.microseconds - Retorna em milisegundos

"""
from datetime import time, date, datetime, timedelta
from dateutil.relativedelta import relativedelta

from pytz import timezone
from os import system
obj = time(11, 50, 30)
print(repr(obj))
print(obj)
print(obj.hour)
print(obj.minute)
print(obj.second)
input('Next:')
system('clear')

obj2 = date(2023, 8, 25)
print(repr(obj2))
print(obj2)
print(obj2.year)
print(obj2.month)
print(obj2.day)
print(obj2.weekday())
input('Next:')
system('clear')

obj3 = datetime.now()

print(obj3.time())
print(obj3.date(), end='\n|')
print(obj3.day, end='|')
print(obj3.month, end='|')
print(obj3.year, end='|\n')
print(obj3.hour, end='|')
print(obj3.minute, end='|')
print(obj3.second, end='|\n')
input('Next:')
system('clear')

data = '08/05/2015 17:21:32'
formato = '%d/%m/%Y %H:%M:%S'

Horastring  = datetime.strptime(data, formato)
print(Horastring)

print(datetime.now(timezone('Asia/Tokyo')))
obj4 = datetime(1969, 12, 31, 21, 00, 00)
print(obj4.timestamp())
print(datetime.fromtimestamp(obj4.timestamp()))
input('Next:')
system('clear')



obj = datetime.now()
obj2 = datetime(2022, 12, 18, 18, 00, 0)
print(obj)
print(obj2)
print(obj - obj2)
print(obj2 > obj)
print(obj > obj2)

prazo = timedelta(days=10)
print('')
print(obj2)
print(prazo)
print(obj + prazo)

intervalo = relativedelta(obj, obj2)
print(intervalo.months)
print(intervalo.days)
print(obj2.strftime('%d/%m/%Y'))

