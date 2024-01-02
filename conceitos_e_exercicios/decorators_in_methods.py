#Substituindo metódo de objeto das classes pela função interna
def my_repr(metodo):
    def interna(self, *args, **kwargs):
        return f'{self.__class__.__name__}({vars(self)})'
    return interna


class SuperTime:
    ...


class Time(SuperTime):
    def __init__(self, nome):
        self.nome = nome

    @my_repr
    def __repr__(self):...


class Planeta():
    def __init__(self, nome):
        self.nome = nome
    @my_repr
    def __repr__(self):...

br = Time('Brasil')
eua = Time('Estados Unidos')

terra = Planeta('Terra')
mart = Planeta('Marte')


print(br)
print(eua)

print(terra)
print(mart)