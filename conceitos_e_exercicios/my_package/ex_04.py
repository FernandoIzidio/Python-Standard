def soma(const):
    def interna(num):
        return const + num
    return interna


def multiplica(const):
    def interna(num):
        return const * num
    return interna


def criar_funcao(funcao, *args):
    return funcao(*args)


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(multiplica_por_dez(80))
print(soma_com_cinco(95))