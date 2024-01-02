"""
Herança uma classe é pai da outra
E as child class herdam todos metódos e atributos da parent class

 Classe principal (Pessoa) - nome, sobrenome, idade, altura
#   -> super class, base class, parent class
# Classes filhas (Cliente) - Endereco
#   -> sub class, child class, derived class

#Method Resolution Order(mro)
O metódo do obj primeiro é buscado na child class, e se não houve é buscado na parent class

"""

class Pessoa:
    def __init__(self, nome:str, idade:int, altura:float, sexo:str):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.sexo = sexo
    

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, altura: float, sexo: str, fidelidade:int):
        super().__init__(nome, idade, altura, sexo) #é criado um objeto na parent class, usando o parametro do init atual
        self.__fidelidade = fidelidade
        self.__endereco = []

    @property
    def fidelidade(self):
        return self.__fidelidade

    def inserir_endereco(self, endereco):
        self.__endereco.append(endereco)


def mostrarattr(obj):
    valores = {chave.replace('_', ' ').strip().split(' ')[-1].capitalize() if '_' in chave else chave.capitalize(): valor for chave, valor in vars(obj).items()}
    for chave, valor in valores.items():
        print(f'{chave}: {valor}' if not isinstance(valor, list) else f'{chave}: {valor[0]}')


client1 = Cliente('Carlão', 68, 1.87, 'Masculino', 4)

client1.inserir_endereco('Rua borracha, Bairro Poste')
mostrarattr(client1)
    


