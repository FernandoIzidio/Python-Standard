"""
pytz.timezone é a melhor classe para pegar timezones prontas, já com dst, utcoffset, fromutc, tzname implementados, é a melhor classe para trabalhar com fuso horários reais

pytz.timezone(timezoneexistente:str)

para verificar timezones existentes: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones


Metódos uteis:
    all_timezones -> list - Retorna todas as timezones válidas de pytz
    all_timezone_set -> set- Retorna todas as timezones válidas em um set
    countrynames ou country_timezones-> Retorna um iterator com todos os paises com timezone

"""
import pytz
from datetime import datetime
PAISES = list(pytz.country_names)
print(PAISES[PAISES.index('BR')])



timezone = pytz.timezone

Recife = timezone('America/Recife')
Tokyo = timezone('Asia/Tokyo')
print(datetime.now(Recife))
print(datetime.now(Tokyo))
