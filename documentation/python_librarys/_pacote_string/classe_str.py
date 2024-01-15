"""
str:
    tabletrans = str.maketrans(oldchar, newchar, delcharsofoldstring) - dict(int:int)
     -Substitui todas as ocorrências de um único caracter, pelo novo caracter em toda a string
     -newchar - 
        - Cria um dict de troca com a representação ascii dos valores antigos como chave, e a representação dos valores ascii novos como valores exemplo:
        {110: 98, 54: 63, ...}
        - Esse dict de chave/valores ascii é usado para fazer substituições com o metódo translate, esse dict é como se fosse um replace melhorado
        - o maketrans pode ser usado varias vezes de forma eficiente, é util em situações onde é preciso fazer varios replaces de forma repetida
        - Nota oldstings e newsstrings precisam ter o mesmo comprimento
    objstr.translate(tabletrans) - Troca os valores antigos pelos novos

"""
texto ='Vou trocar todas letras "A" da string, a troca acabou de começar, a seguir varias letras "A\'s" de exemplo a a a a a a ' 

table = str.maketrans('a','5')
flag = texto.index('a seguir')
print(texto[0: flag] + texto[flag: -1].translate(table))


