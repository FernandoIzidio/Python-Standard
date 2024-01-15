"""
tzinfo - : É uma classe abstrata, que serve para definir informações de fuso horário personalizadas. É muito util quando se pretende criar um objeto datetime com fusohorario personalizado

Metódos uteis de tzinfo:
    utcoffset(self, dt): Este método deve retornar o deslocamento UTC (Tempo Universal Coordenado) para um determinado objeto datetime. O brasil tem deslocamento de tempo universal cordenado -3 UTC tem que retornar timedelta para indicar o deslocamento utc do objeto

    dst(self, dt) -datetime summer time- Este metódo deve retornar o deslocamento utc de um objeto datetime no horario de verão, ou seja tem que mostrar o UTC no horario de verão
    se não tiver horario de verão retornar o horario padrão

    tzname(self, dt): Este método deve retornar um nome descritivo do fuso horário para um objeto datetime

    fromutc(self, dt): Este é o método responsavel por alterar a timezone de um objeto datetime, o metódo astimezone(tz) usa esse metódo para alterar a timezone de um objeto datetime



"""
from datetime import datetime, timedelta, tzinfo, timezone


class MyPersonFuso(tzinfo):
    def utcoffset(self, __dt: datetime | None) -> timedelta | None:
        return timedelta(hours=-4)
    
    def dst(self, __dt: datetime | None) -> timedelta | None:
        return timedelta(hours=-5)
    
    def tzname(self, __dt: datetime | None) -> str | None:
        return 'UTC-04'
    

chinahour = timezone(timedelta(hours=9), 'UTC+09')
print(datetime.now(MyPersonFuso()))
print(datetime.now(chinahour))

