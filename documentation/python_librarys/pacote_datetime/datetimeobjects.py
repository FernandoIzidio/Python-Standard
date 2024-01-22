"""
datetime, classe muito robusta para manipulação de tempo.

datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0) Argumentos de inicialização/construção de um objeto datetime

Metódos uteis:
    today() - Faz a mesma coisa que o now, retorna data e hora atual conforme o fuso horario

    now() - Retorna o horário atual

    utcnow() - Retorna o tempo universal, utc 0, ou seja retorna o tempo universal atual sem fuso-horário

    fromtimestamp(timestamp) - Cria um objeto datetime a partir de um timestamp

    utcfromtimestamp(timestamp) - Retorna o horário universal, a partir de um timestamp, não precisa ser o timestamp do horário universal, pode ser um timestamp com fusohorario, e mesmo assim ele retornará o horário universal, a partir de um timestamp
    
    timestamp() - Retorna o timestamp em segundos da data atual

    
    fromordinal(days) - Cria um objeto datetime, a partir do número de dias após o dia 01/01/0001

    fromisoformat(AAAA-MM-DD:str) - Cria um objeto datetime, a partir de uma data no formato ISO

    fromisocalendar(year, week, weekday) - Cria um objeto datetime, a partir do ano, o número da semana e o dia da semana, exemplo cria um objeto datetime a partir do quarto dia da terceira semana de 2020


    strptime(data_string, formato) -> datetime - Cria um objeto datetime, a partir de uma data em string, e formato em string

    strftime(formato)-> str - Formata um objeto datetime para um formato em especifico

    utctimetuple() - Retorna a representação de um objeto datetime no formato struct_time, util para converter de volta para timestamp

    utcoffset() - Retorna o deslocamento utc positvo ou negativo(timedelta), de um objeto datetime    

    datetime.combine(date, time) - Cria um objeto datetime, a partir de dois objetos time, e date


    datetime.date() - Retorna a parte da data de um objeto datetime
    datetime.time() - Retorna a parte time de um objeto datetime

    datetime.fold - Lida com a questão de dobra de horas, na transição do horario de verão pro padrão, ou do padrão pro verão, se fold retornar 0 é porque é a primeira ocorrência da hora no dia, se retornar 1 é a segunda ocorrência da hora no dia

    datetime.replace(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0) - Se receber algum valor novo, substitui valores antigos de um objeto datetime, por valores novos para o objeto datetime


    datetime.dst - Retorna 0 se o objeto datetime não está no horário de verão, ou retorna um timedelta com o delocamento utc, se o objeto datetime está no horário de verão

    datetime.astimezone(timezone) -  Altera a timezone/fusohorário de um objeto datetime para outra timezone/fusohorário, em outras palavras, esse metódo ALTERA a timezone de um objeto de datetime

    utctimetuple() - Retorna a representação struct_time, de um objeto datetime universal
    timetuple() - Retorna a representação struct_time, de um objeto datetime local


    toordinal() -> int - Retorna o número de dias após o dia 01 de janeiro 0001 de um objeto datetime

    weekday() - Dia da semana de um objeto datetime, 0 segunda, 6 domingo

    isoweekday() - Retorna o dia da semana no formato ISO de um objeto datetime, os dias da semana no formato ISO, 1 é segunda feira, e 7 é domingo


    isoformat() - Retorna a representação string de um objeto datetime, no formato ISO

    isocalendar() - Retorna a representação string de um objeto datetime, no formato ISOCALENDAR, exemplo datetime equivale ao terceiro dia da segunda semana de 2021 (2021, 2, 3)

    ctime() - Retorna uma representação mais legivel de um objeto datetime 

    tzname() int/str - Retorna o nome descritivo de uma timezone, esse nome descritivo, é o deslocamento utc em relação ao tempo universal

Operações suportadas: 
    datetime2 = datetime1 + timedelta
    datetime2 = datetime1 - timedelta
    timedelta = datetime1 - datetime2
    bool = datetime op_relacional datetime2
    
    """


from datetime import datetime, timedelta, timezone as tz
from pytz import timezone

print(datetime.utcnow())
print(datetime.today())
print(datetime.now())
print(datetime.now().timestamp())

timestampuniversal = datetime.utcfromtimestamp(datetime.now().timestamp())
print(timestampuniversal)
print(datetime.fromordinal(10))

print(datetime.now().utctimetuple()) # Retorna representação struct_time, do objeto datetime
print(datetime.now(timezone("America/Sao_Paulo")).utcoffset()) #Retorna o deslocamento utc da timezone são paulo, falta 3 horas para 0 horas, então o deslocamento utc de são paulo é -3, utc 0 é o tempo universal

print(datetime.now().date())
print(datetime.now().time())


dt1 = datetime(2023, 10, 29, 1, 30, 0, 0, fold=0)

print(dt1, dt1.fold)
dt1 = dt1 + timedelta(hours=1)
dt1 = dt1 - timedelta(hours=1)
  
print(dt1, dt1.fold)


print(datetime.now(timezone("America/Sao_Paulo")).dst())


japao = tz(timedelta(hours=9), 'timezone_japao')
localtime = datetime.now()
formatolatino = "%d/%m/%Y %H:%M:%S"
universaltime = datetime.now(tz.utc)

print(localtime.strftime(formatolatino))
print(localtime.astimezone(japao).strftime(formatolatino))
print(universaltime.utctimetuple())
print(universaltime.timetuple())

print(datetime.now(timezone("America/Sao_Paulo")).tzname())

