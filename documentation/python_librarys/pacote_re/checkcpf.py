from random import randint
import re
def get_cpf():
    def interna(cpf):
        cpf = str(cpf)
        real = ' '.join(cpf.split('.'))
        real = ' '.join(real.split('-')).split(' ')
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False
        
        if [cpf[:3] == parte for parte in real[:3]].count(True) >= 2:
            return False
        

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = 11 - (soma % 11)
        if resto == 10 or resto == 11:
            resto = 0
        if resto != int(cpf[9]):
            return False
        
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = 11 - (soma % 11)
        if resto == 10 or resto == 11:
            resto = 0
        if resto != int(cpf[10]):
            return False
    
        return True
    
    while True:
        cpf = f"{f'{randint(100,999)}.{randint(100,999)}.{randint(100,999)}'}".strip('.')+f'-{randint(0,99)}'

        if interna(cpf):
            return cpf

with open('cpf.txt', 'w', encoding='utf-8') as filetext:
    filetext.writelines([get_cpf()+'\n' for count in range(10000)])
