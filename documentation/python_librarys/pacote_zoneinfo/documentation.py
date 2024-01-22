"""
O módulo ZoneInfo permite lidar com fuso horários reais, assim como o timezone do pytz

O módulo ZoneInfo surgiu a partir da versão 3.9 e ofereça uma solução concisa para trabalhar com fuso horários reais

A base de dados do Zone Info é a IANA(Internet Assigned Numbers Authority)

https://timeapi.io/documentation/iana-timezones - API que lista todas as timezones da base de dados da IANA

"""
import zoneinfo
import datetime

formato = "%d/%m/%Y %H:%M:%S"

universaltime = datetime.datetime.utcnow()
localtime = datetime.datetime.now()

cbzone = zoneinfo.ZoneInfo("Africa/Casablanca")
cbtime = localtime.astimezone(cbzone)

print(universaltime.strftime(formato))
print(localtime.strftime(formato))
print(cbtime.strftime(formato))
print(cbtime.dst())
print(cbtime.tzname())