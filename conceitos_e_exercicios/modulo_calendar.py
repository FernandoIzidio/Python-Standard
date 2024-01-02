"""
monthrange -> Retorna o primeiro e ultimo dia do mês
calendar(year) -> Retorna o calendário de um ano
month(month) -> Retorna o calendário de um mês
day_name -> Retorna uma lista com os nomes dias da semana
monthcalendar -> Retorna uma lista de tuplas, que tem dia do mês e semana
"""
import calendar

print(calendar.calendar(2021))

print(calendar.monthrange(2020, 12))

print(calendar.day_name[calendar.monthrange(2020, 12)[0]])