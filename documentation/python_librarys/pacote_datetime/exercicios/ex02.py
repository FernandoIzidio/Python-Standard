"""
Emprestimo: 1_000_000
Tempo para pagar: 5 anos
Numero de Parcelas : 60

"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

datainicio = datetime.now()
datafim = datainicio + relativedelta(years=5)

money_loan = 1_000_000
month = relativedelta(months=1)
installment = 1_000_000 / 60

formato = "%d/%m/%Y %H:%M:%S"

count = 1
while datainicio <= datafim:
    print('='*50)
    print(f'Paracela {count}'.center(50, ' '))
    print('='*50)
    print(f'Prestação: R${installment:-.2f}'.replace('.', ',').replace('-', '.'))
    datainicio += month
    print(f'Vencimento: {datainicio.strftime(formato)}')
    input()
    count += 1
    if count > 60:
        break