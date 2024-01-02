from dotenv import load_dotenv
import os
load_dotenv()
cargos = {os.getenv('SENHA1'): 0.05, os.getenv('SENHA2'): 0.10, os.getenv('SENHA3'): 0.20}
compra = float(input('Informe o valor da compra: '))
senha = input('Informe a senha: ')
desconto = int(input('Informe o percentual de desconto: '))

if cargos.get(senha) != None:
    if desconto <= cargos.get(senha) * 100:
        percent = cargos.get(senha)
        print(f"""Desconto permitido: até {percent * 100}%
        Valor total da compra: R${compra:.2f}
        Valor do desconto: R${compra * percent:.2f}
        Valor com desconto: R${compra - (compra * percent):.2f}""".replace('.', ','))
    else:
        print(f"""Desconto permitido: até {cargos.get(senha) * 100}%
Erro: Você não pode aplicar um desconto maior que {cargos.get(senha) * 100}%!""")
else:
    print('Você não tem permissão para aplicar descontos.')