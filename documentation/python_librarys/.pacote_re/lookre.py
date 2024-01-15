"""
Retorna uma palavra, se tiver determinada palavra a frente ou a atrás de uma palavra desejada
(?=value) - Define se determinado grupo a frente ou atrás tem que ter algum valor

LOOK BEHIND OU LOOK AHEAD NÃO RETORNAM A PALAVRA, APENAS CHECAM SE A PALAVRA EXISTE ANTES OU DEPOIS DA EXPRESSÃO REGULAR, E RETORNARM AS EXPRESSÕES QUE CORRESPONDEREM A TODAS CONDIÇÕES

"""
import re

host = """
ONLINE 192.168.0.1 GHIJK active
OFFLINE 192.168.0.2 GHIJK inactive
OFFLINE 192.168.0.3 GHIJK active
ONLINE 192.168.0.4 GHIJK active
ONLINE 192.168.0.5 GHIJK inactive
OFFLINE 192.168.0.6 GHIJK active
"""
print("IP'S registrados:", end='\n\t')
print(*re.findall(r'\w+\s*((?:[\d]{3}\.){2}\d\.\d)', host), sep='\n\t')

print('\n')
print("IP'S ativos:", end='\n\t')
print(*re.findall(r'\w+\s*((?:\d{3}.){2}\d.\d)\s*\w+\s*(?=active)', host), sep='\n\t') #Busca todas as ocorrências que correspondam a expressão regular
print('\n')
print("IP'S desativos: ", end='\n\t')
print(*re.findall(r'\w+\s*((?:\d{3}\.){2}\d\.\d)\s*\w+\s*(?=inactive)', host), sep='\n\t')
print('\n')
print('Ips:', end='\n\t')
print(*re.findall(r'(?=.*inactive).*', host), sep='\n\t')

print('Ips:', end='\n\t')
print(*re.findall(r'(?=.*active)(?:[0-9]{3}.){2}[0-9].[0-9]', host), sep='\n\t')

print('Online:', end='\n\t')
print(*re.findall(r'(?<=ONLINE).*', host), sep='\n\t')

print('Offline:', end='\n\t')
print(*re.findall(r'(?<=OFFLINE).*', host), sep='\n\t')
