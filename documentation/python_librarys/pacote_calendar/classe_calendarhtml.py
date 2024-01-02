"""
Gera calendários personalizados no formato html
    formatmonth(year, month, incluianocabecalho:bool)  - retorna o calendário de um mês no formato html

    formatyear(year)->str - Retorna um calendário de um ano, em formato table html

    yeardatescalendar(theyear, width=3) - Retorna uma lista de calendários html para todos meses do ano

    formatyearpage - Retorna um calendário de um ano, como uma página HTML completa
"""


import string

import calendar
from pathlib import Path
header = calendar.HTMLCalendar(0)
waydir = Path(__file__).parent / "index.html"
calendar2020 = header.formatyear(2020).splitlines()


def findlinefalse(line:str):
    if not line.translate(line.maketrans(string.whitespace, string.whitespace, string.whitespace)):
        return False
    return True

with open(waydir, 'r', encoding='utf-8') as index:
    conteudo = index.read().splitlines()
    end = conteudo.index('</body>')    
    
    if not findlinefalse(conteudo[end - 1]):
        for pos, linha in enumerate(calendar2020):
            conteudo.insert((end - 1)+pos, linha)

with open(waydir, 'w', encoding='utf-8') as index:
    index.write('\n'.join(conteudo))
      

