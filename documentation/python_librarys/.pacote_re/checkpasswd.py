"""
"""
import string, random, re, os
passwd = '' + string.ascii_letters + string.punctuation + string.digits

print(*[''.join(random.sample(passwd, 8)) for count in range(12)], sep='\n')

while True:
    os.system('cls')
    passw = input('Digite uma senha: ')
    if re.findall(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%¨¨\'\"&*\(\)\\/^´~\[\];:+|,\.=_]).{12,}', passw):
        print('Senha forte passou.')
        break
    input('Senha fraca, tente novamente, pressione qualquer tecla pra avançar: ')

