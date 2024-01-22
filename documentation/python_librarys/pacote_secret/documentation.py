"""
Secrets gera números aleatórios seguros

É util para geração de tokens, senhas, segurança, criptografia e etc

secrets:
    randbelow(value) - Retorna números aleatórios abaixo de value 
    SystemRandom() - Retorna um obj random seguro

Objetos ramdom gerados por systemrandom são mais seguros, e perdem a função seed
"""
import secrets
import string


random = secrets.SystemRandom()

print(random.randint(0,100))

senha = random.choices(string.ascii_letters + string.digits + string.punctuation, k=20)
print(''.join(senha))