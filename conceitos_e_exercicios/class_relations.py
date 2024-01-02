"""
Associação - Relação fraca entre classes, quando o ciclo de vida, metódos atributos de uma não dependem de outra classe
Ex: um atributo recebe como valor um obj de uma outra classe


Agregação - Relação média entre classes, quando uma classe depende da outra, para retornar um atributo, ou executar um metódo


Composição - Relação forte entre classes, quando o ciclo de vida de uma classe depende da outra

"""


class Escritor:
    def __init__(self, nome, ferramenta) -> None:
        self.__nome = nome 
        self.__ferramenta = ferramenta

    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, valor):
        self.__ferramenta = valor

    def escrever(self):
        print(f'{self.nome} está escrevendo com {Ferramentas(self.ferramenta).nome}' if isinstance(self.ferramenta, str) else f'{self.nome} está escrevendo com {self.ferramenta.nome}')

class Ferramentas:
    def __init__(self, nome) -> None:
        self.nome = nome 

    def manutencao(self):
        print(f'{self.nome} está em manutenção')

art = Escritor('Picasso', 'Pincel')
art.escrever()
bic = Ferramentas('Caneta')
art.ferramenta = bic
art.escrever()
art.ferramenta.manutencao()
bic.manutencao()
art.escrever()