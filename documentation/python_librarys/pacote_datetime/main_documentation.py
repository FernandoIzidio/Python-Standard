"""
pytz - timezone(nameofregion) - Pega timezones prontos

Melhor módulo para manipulação de tempo:

Metódos uteis do módulo datetime:
    MINYEAR - Ano minimo para criar um objeto da classe datetime
    MAXYEAR - Ano máximo para cirar um objeto da classe datetime
    UTC - Retorna o fuso-horario local
    
UTC = Universal Time Cordenate - Tempo universal cordenado

Principais classes da biblioteca datetime:
    date - é uma classe que cria objeto do tipo date, o init recebe valores como year, month, day
    
    time - é uma classe que cria objeto do tipo time, o init recebe valores como hour, minutes, seconds, microseconds e etc

    datetime - É uma combinação das classes date e time, e tem como valores inicializadores, year, month, day, hour, minute, seconds, microseconds e etc

    timedelta - É uma classe que expressa a diferença de tempo entre dois objetos date e time, ou dois objetos datetime

    tzinfo - Uma classe abstrata usado para criar objetos timezone de forma personalizada, é muito util quando se quer personalizar o calculo de fuso-horários, horários de verão, e nomes descritivos de fuso horários, é preciso definir o utcoffset(deslocamento de tempo utc), dst(deslocamento no summer time, também tem que ser um timedelta para expressar quantas horas ele se desloca do utc), tzname(nome descritivo da timezone)

    timezone(utcoffset, tzname) - É uma child class da classe abstrata tzinfo, permite criar um objeto timezone personalizado, usado para modificar o fuso horário de um objeto datetime

As classes date, datetime, time, and timezone:
    São objetos imutaveis
    São hashaveis, ou seja podem ser usados como chave de dicionário

    
Objetos ingênuos:
    Um objeto das classes datetime e time sempre serão ingênuos
    
obs: Um objeto datetime e time só serão conscientes, quando a timezone não for none, e o deslocamento utc (utcoffset) não for none.

Objetos consciêntes tem timezone
objetos ingênuos não tem timezone
"""

import datetime
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
print(datetime.UTC)

obj = datetime.datetime.now()
print(obj)

