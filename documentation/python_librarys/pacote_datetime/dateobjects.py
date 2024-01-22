"""
ISO - Organização Internacional de Normalização/Padronização (International standard organization)

date é uma classe simples para trabalhar com manipulação de tempo em anos, meses e dias

date = date(year, month, day) - Todos argumentos são obrigatórios e devem ser inteiros, seguindo determinados ranges, mes tem que estar entre 1 e 12, dias 1 e lasdaymonth, ano 1 e maxyear


Metódos e atributos uteis:
    today() - Retorna a data atual
    strftime(formato:str) - str - Formate um objeto date, e retorna o objeto date formatado(str) em um determinado formato
    
    fromtimestamp(timestamp: seconds) - Cria um objeto date/datetime/time, a partir de um timestamp especifico
    
    fromordinal(day: int) - Cria um objeto date/datetime, a partir do número de dias após o dia 01/01/0001
    
    fromisoformat(AAAA-MM-DD: str) - Cria um objeto date/datetime, a partir de uma string que siga o formato ISO, exemplo 2012-05-30
    
    fromisocalendar(year, week, weekday) - Cria um objeto date/datetime, a partir de um dia da de determinada semana de um ano, exemplo cria um objeto datetime a partir do terceiro dia da quarta semana de 2014

    
    min - menor data possivel
    max - maior data possivel
    resolution - menor diferença possivel entre dois objetos date diferentes (1 day)

    year ->int - retorna o ano data
    month -> int - Retorna o mês da data
    day -> int - Retorna o dia da data

    replace(year, month, day) -> datetime - Troca os valores de um objeto datetime, e retorna esse objeto datetime com valores alterados

    date.timetuple() - Converte um objeto date para o formato struct_time, pode ser util quando se deseja converter para o formato unix.timestamp
    
    date.toordinal() - int - Retorna o número de dias desde o dia 1 de janeiro de 0001

    date.weekday() int - Retorna o dia da semana correspondente a uma data

    date.isoformat() - Retorna a data no formato iso  AAAA-MM-DD

    date.isocalendar() - tuple - Retorna uma tupla contendo o ano, número da semana, e dia da semana de uma determinada data

    date.ctime() - str - Isso retornara a data em um formato legivel para humanos

Operações suportadas:
    date = date + timedelta -> Retorna um novo objeto a partir de um deslocamento de tempo
    date = date - timedelta -> Retorna um novo objeto a partir de um deslocamento de tempo
    timedelta = date - date2 -> Cria um deslocamento de tempo, a partir de dois objetos do tipo date, ou seja cria a diferença de tempo entre dois objetos date
    date < date2 -> Checa se uma data antecede a outra, se a data for antes, essa data sera menor que a outra data. o mesmo vale para qualquer outro operador relacional

    
"""

from datetime import date

hoje = date.today()
print(hoje)
print(hoje.strftime('%d/%m/%Y'))
print(date.fromtimestamp(500))
print(date.fromordinal(366))
print(date.fromisoformat("2020-05-27"))
print(date.fromisocalendar(2014, 5, 1))
print(hoje.year, hoje.month, type(hoje.day))

print(hoje.replace(2024))

d = date(2023, 10, 27)
timetuple = d.timetuple()
print(timetuple)

print(hoje.toordinal())
print(date.fromordinal(1000000))

print(hoje.weekday())

print(hoje.isocalendar())

print(hoje.ctime())