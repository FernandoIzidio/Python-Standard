"""
Tipos de funções:
- First-Class-Function
Funções de primeira classe são funções que são tratadas como tipo de dados pois retornam string,int float, bool e etc

-High-Order-Function
São funções que retornam outras funções como valores de retorno, são as populares closure functions
"""

def somar(x, y):
    return x + y


print(somar(8,6))



def multiplicar(const):
    def interna(num):
        return num * const
    return interna

dobrar = multiplicar(2)
print(dobrar(64))