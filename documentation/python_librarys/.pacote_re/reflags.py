"""
flags:
    re.I ou re.IGNORECASE - Expressão regular não vai diferenciar maiusc de minusc
    re.A ou re.ASCII - Expressão regular vai pegar apenas expressões em ASCII
    re.Multiline re.M - Expressão regular vai analisar string linha a linha
    re.S - quantificadores passam a reconhecer/incluir quebra de linha
    re.X - Permite comentar dentro da expressão regular
[À-úA-Za-z0-9] ou \w
[^Á-úA-Za-z0-9] ou \W - Vai retornar toda ocorrência que for diferente disso
[0-9] ou \d
[^0-9] ou \D
[ \n\t\r] ou \s
[^ \n\t\r] ou \S
\b - antes/depois tem uma string vazia ou espaço, border
\B - Não pode ter antes/depois da palavra uma string vazia ou espaço, no border
"""
import re
texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo. Magia
0aria
Não canso de ouvir a Maria: mafia
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'.+', texto)) #Vai fechar um item na ultima ocorrência de fechamento
print(re.findall(r'.*?', texto)) #Vai fechar um item na primeira ocorrência
print(re.findall(r'[a-z]+', texto, re.IGNORECASE)) # Apenas codificação ASCII
print(re.findall(r'\w+', texto, flags=re.IGNORECASE))
print(re.findall(r'\bflo\w+', texto))
print("4 Letras:", re.findall(r'\b\w{4}\b', texto, re.I))
print(re.findall(r'\Blore\B', texto, re.I))

texto2 = """O João gosta de folia 
E adora ser amado"""

print(re.findall(r'^o.*o$', texto2, flags=re.I|re.S))