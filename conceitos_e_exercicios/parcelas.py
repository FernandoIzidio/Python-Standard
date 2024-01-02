from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


parcela = 1000000 / 60
#5 anos
dataemprestimo = '20/12/2020'
formato = '%d/%m/%Y'

datas = []
anoemprestimo = datetime.strptime(dataemprestimo, formato)
prazo = relativedelta(years=5)
fimemprestimo = anoemprestimo + prazo
dataparcela = anoemprestimo

while dataparcela < fimemprestimo:
    print(f'Valor Parcela: R${parcela:,.2f}'.replace('.', ',', 1) + f'. Vencimento {dataparcela}')
    dataparcela += relativedelta(months=+1)
