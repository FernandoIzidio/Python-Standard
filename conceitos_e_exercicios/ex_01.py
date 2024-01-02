# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def multiplicar(const):
    def interna(num):
        return num * const
    return interna

dobrar = multiplicar(2)
triplicar = multiplicar(3)
quadriplicar = multiplicar(4)

print(dobrar(2))
print(triplicar(2))
print(quadriplicar(2))