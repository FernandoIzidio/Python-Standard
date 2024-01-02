from dateutil.relativedelta import relativedelta
from datetime import datetime

emprestimo = 1_000_000
parcelas = emprestimo / 60
data = '20/12/2020'
format = '%d/%m/%Y'
duracao = relativedelta(years=5)
datainicio = datetime.strptime(data, format)
datafim = datainicio + duracao
dataatual = datainicio
count = 0
while not dataatual >= datafim:
    print(f'Parcela {count+ 1}')
    print(f'Parcela: R${parcelas:.2f}'.replace('.',',') + '.')
    dataatual = dataatual + relativedelta(months=1)
    print(f'Data de Pagamento: {dataatual}')
    count += 1 