"""
Ao tratar de entradas de dados, para fazer uma aplicação segura é essencial sempre validar a entrada de dados, SQLINJECTION.

Exemplo de validação:
entrada = input()

if len(entrada) < 9:
    numero = int(entrada)
else:
    print('ERRO: Limite de algarismo excedido')

    
sys.get_int_max_str_digits() - Retorna o limite de algarismo padrão para conversão de str em int
sys.set_int_max_str_digits() - Define um novo limite de algarismo para conversão de str em int
"""
import sys

print(sys.get_int_max_str_digits())