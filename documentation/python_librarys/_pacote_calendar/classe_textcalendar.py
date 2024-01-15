"""
Permite criar calendários personalizados no formato txt

formatmonth(theyear, themonth, w=0, l=0) -str - Retorna o calendário de um mês em especifico no formato str, w é a largura de cada coluna, l é o número de linhas para uma semana

prmonth(year, month, w, l) - Imprime o calendário de um mês no console

formatyear(theyear, w=2, l=1, c=6, m=3) - Retorna o calendário de um ano em especifico no formato str

pryear(theyear, w=2, l=1, c=6, m=3) - Imprime o calendário de um ano inteiro no terminal

w - largura das colunas
l - número de linhas que uma semana vai ter
c - espaçamento entre colunas
m - Número de colunas meses do calendário

"""

from calendar import TextCalendar


calendario = TextCalendar()

print(calendario.formatmonth(2023, 8))
calendario.prmonth(2023, 6)
print(calendario.formatyear(2023, m=4))