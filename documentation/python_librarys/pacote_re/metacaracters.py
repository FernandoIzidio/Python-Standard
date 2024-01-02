"""
Meta caracters:
    | - ou
    . - qualquer caracter exceto quebra de linha
    [] - Conjunto de caracters definidos, apenas um caracter é escolhido
    chr-chr - É usado para criar um range de caracters
    () - Conjunto de cadeias, ou seja a expressão só vai ser correspondida se corresponder ao grupo inteiro
    ^ - Começa com caracter/expressão
    $ - Termina com caracter
flags - Mexe com as configurações de uma expressão regular
    flags = re.Ignorecase - Não diferencia maiusculo de minusculo
    [^d-f] - Dentro de colchetes esse acento circunflexo significa negação, ou seja qualquer caracter
    que não esteja entre d e f


Quantificadores: 
    * - caracter pode se repetir 0 ou n vezes
    + - caracter pode se repetir 1 ou n vezes
    ? - caracter pode se repetir 0 ou 1 vezes
    {n} - Quantidade definida
    {n,} - N ou mais vezes
    {,n} - 0 até n vezes

    {n, n} - Intervalo

findall() - Retorna todas as ocorrências de um expressão, é um padrão guloso

Em empressões ambiguas ou seja expressões que podem ter varios fechamentos, usa-se ? para garantir que o quantificador feche na primeira correspondência de fechamento

para corigir expressões quantificadores gulosos usa-se ? para garantir que a ocorrência feche na primeira correspondência



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

print(re.findall(r'João|Maria|ad.ltos', texto))
print(re.findall(r'[Jj]oão|[Mm0-9]a[a-zA-Z]ia|ad[a-z]ltos', texto))
print(re.findall(r'João|Maria', texto, flags=re.IGNORECASE))

print(re.findall(r'[Jj]o*ão*', texto))
print(re.sub(r'[Jj]o*ão*', 'Tulio', texto))
print(re.findall(r'.*', texto))


html = "<p>Frase</p> <p>Eita</p> <p>Trucoooooo</p> <div>Pegaaaa a LAPADAAAAA</div>" 

print(re.findall(r'<[pdiv]{1,3}>.*?<\/[dpiv]{1,3}>', html))

