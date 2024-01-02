"""
Calendar módulo excelente para trabalhar com calendários

Metódos uteis

    calendar(year) - Retorna o calendário de um ano
    month(year, month)- Retorna o calendário de um mês de um ano

    monthrange(year, month) - Retorna dia da semana em que começa o mes, e ultimo dia do mês

    day_name - Retorna lista com os nomes dos dias da semana
    month_name - Retorna uma lista com os nomes dos meses de um ano
    day_abbr - Retorna lista com os dias da semana abreviados
        0 segunda feira -6 domingo

    weekday(year, month, day) - Retorna o dia da semana de uma data

    monthcalendar(year, month) - Retorna o calendário no formato semanas, ou seja todos dias distruibuidos em semanas



classe calendar - Oferece varios iterators para iterar sobre datas de forma customizada
    
classe TextCalendar:
    Util para criar calendários em txt

    
classe calendar HTML - Util para criar calendários para páginas html

    """


import locale
import calendar
from os import system




print(calendar.calendar(2023))
print(list(enumerate(calendar.day_name)))
print(list(calendar.day_abbr))

print(calendar.month(2023, 8))
firstweekdaymonth, lastdaymonth = calendar.monthrange(2023, 8)
print(calendar.day_name[firstweekdaymonth])
print(calendar.day_name[calendar.weekday(2023, 8, lastdaymonth)])

print()
print(calendar.month(2023, 10))
firsweekday, lastdaymonth = calendar.monthrange(2023, 10)
print('Primeiro dia semana: ', calendar.day_name[firsweekday])
print('Número de dias do mês: ', lastdaymonth)
print('Ultimo dia do mês: ', calendar.day_name[calendar.weekday(2023, 10 ,lastdaymonth)])
