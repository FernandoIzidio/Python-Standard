"""
Metódos de objetos da classe calendar:
    classe calendar - Possui vários iterators para iterar sobre datas de um mês/ano em vários formatos

    Tem muitos iterators para iterar sobre datas de meses, e anos de forma personalizada


    firstweekday - Número equivalente ao primeiro dia da semana no calendário

    iterweekdays iter(int) -  Retorna um iterator númerico de mesmo comprimento day_name, para iterar sobre todos os dias de uma semana
    
    itermonthdates(year, month) iter(datetime) - Retorna um iterator datetime com as datas em todas as semanas que tenham datas do mês, é tipo um monthcalendar mas com objetos datetime

    itermonthdays(year, month) iter(int) - iterator númerico semelhante ao monthcalendar, mas sem dividir cada semana por uma lista.

    itermonthdays2(year, month) iter(tuple) - Similiar ao monthcalendar, mas retorna um iterator de tuplas (diadomês, diadasemana), os dias que não pertencerem ao mês escolhido vão ter valor 0.

    itermonthdays3(year, month) iter(tuple) - Similiar ao month calendar, mas retorna um iterator de tuplas (ano, mês, dia), todos os dias tem valor independente de fazerem parte ou não do mês escolhido

    itermonthdays4(year, month) iter(tuple) - É uma junção do itermonthdays2 e itermonthdays 3, retorna um iterator de tuplas(ano, mês, dia, dia da semana)
    
    monthdatescalendar(year, month) - list[list[datetime]] - Similiar ao itermonthdate, retorna um iterator de objetos datetime em todas as semanas que tenham dias do mês escolhido. Porém 
    separa cada semana por uma lista de objetos datetimes

    monthdayscalendar(year, month) - faz a MESMA coisa que monthcalendar

    monthdays2calendar(year, month) - faz a mesma coisa que o itermonthdays(2), mas separa cada semana por uma lista

    yeardatescalendar(year, width(para agrupar meses, o padrão é 3 meses para cada lista)) - Retorna uma lista de objetos de objetos datetime em todas as semanas que tenham pelo menos um dia do ano.

    yeardayscalendar(year, width) - semelhante ao yeardatescalendar, mas ao invés de retorna objetos datetime, retorna lista de agrupamento de mês lista de mês lista(semanas) int's e os dias que não pertencerem ao ano vão ter valor 0

    yeardays2calendar(year, width) - Semlhante ao yeardayscalendar, mas ao inves de retorna listas de número inteiros, retorna lista de tuplas(dia do mês, dia semana), se o dia não pertencer ao ano, vai ter valor 0



"""
import calendar

calendario = calendar.Calendar(0)

calendario = calendar.Calendar(0)
print(list(calendar.Calendar().itermonthdays(2020, 12)))
input()
print(list(zip(calendario.iterweekdays(), calendar.day_name)))
print('\n\n')
print(f"{list(calendario.itermonthdates(2020, 2))}  {len([dia for semana in calendar.monthcalendar(2020, 2) for dia in semana])}")
print('\n\n')
print(list(calendario.itermonthdays(2020, 2)))
print('\n\n')
print(list(calendario.itermonthdays2(2020, 2)))
print('\n\n')
print(list(calendario.itermonthdays3(2020, 2)))
print('\n\n')
print(list(calendario.itermonthdays4(2020, 2)))
print('\n\n')
print(calendario.monthdatescalendar(2020, 2))
print('\n\n')
print(calendario.monthdayscalendar(2020, 2))
print('\n\n')
print(calendario.monthdays2calendar(2020, 2))
print('\n\n')
print(calendario.yeardatescalendar(2020))
print('\n\n')
print(calendario.yeardays2calendar(2020))
