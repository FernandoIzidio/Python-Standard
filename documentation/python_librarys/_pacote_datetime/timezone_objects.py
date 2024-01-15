"""
timezone é uma child class da classe abstrata tzinfo, permite manipulação de fuso-horários de forma simples, sem levar em conta regras de fuso-horário e outras variações

timezone(timedelta(deslocamento do UTC), nomedescritivo(utc+-num)) - Retorna uma timezone/fusohorario

"""
from datetime import timezone, datetime, timedelta

japaozone = timezone(timedelta(hours=9), 'UTC+09')
localtime = datetime.now()
universaltime = datetime.now(timezone.utc)
japaotime = datetime.now(japaozone)


print('Tempo universal:', universaltime)
print('Tempo local:    ', localtime)
print('Tempo japão:    ', japaotime)