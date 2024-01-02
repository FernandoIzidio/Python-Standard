"""
Uma classe é a responsável, por definir atributos, metódos de um objeto
Ou seja uma classe vai gerar vários objetos
E todos os objetos de uma classe vão herdar seus atributos e metódos
Encapsulamento:
    nome sem underlina:
    public
    disponiveis em todo o código

    nome com um underline:
    Protected
    Disponivel no escopo da classe e subclasses

    nome com dois underline:
    Private
    Disponiveis somente no escopo da parent classe

@Classmethods
São metódos da classe
São uteis para criar objs já com atributos prédefinidos, ex 

@Staticmethods 
São metódos que não recebem nem o objeto self, nem a classe cls, como primeiro parametros, esses metódos se comportam como uma função protegida pelo namespace da classe, ou pelo namespace do objeto
se comportam exatamente como funções porém dentro do escopo da função
podem ser uteis para importação, mas não muito uso além disso



class Pessoa:
    def __init__(self) -> None:
        ...

    @classmethod
    def senhor(cls, ...):
        temp = obj(..., idade=60, sexo=masculino)
        return temp

Esse metódo senhor da classe pessoas, cria um obj com os atributos idade e sexo predefinidos

-Classes também podem ter atributos

@property
São metódos que se comportam como atributos

@atributo.setter
Permite que o usuário mude o valor de um atributo property

def property(self, valor)
    self.attr = valor

OBS: Setters não podem retornar valores
    
dir(obj)-Retorna todos atributos e metódos do obj

__dict__ -Retorna os atributos do objeto

vars(obj) - Retorna os atributos do objeto
"""
from datetime import datetime


from json import dump
from os import system

class Carro:
    ano = datetime.now().year
    def __init__(self, fabricante, nome, preco, potencia) -> None:
        self.__fabricante = fabricante
        self.__nome = nome
        self.__preco = preco
        self.__potencia = potencia
    
    @property
    def fabricante(self):
        return self.__fabricante

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def potencia(self):
        return self.__potencia     
    
    @property
    def velocity(self):
        return self.__velocity    

    def acelerar(self):
        self.__velocity = 60
        print(f'{self.nome} está acelerando')

    @classmethod
    def popular(cls, fabricante, nome):
        temp = cls(fabricante, nome, 50000, 150) 
        return temp      

    @classmethod
    def roncar(cls):
        print('BRUM BRUM BRUM BRUUUUUUUUUUUM')

    @velocity.setter
    def velocity(self, valor):
        self.__velocity = valor
   


print(f'Ano atual é: {Carro.ano}')
car = Carro('Volkswaggen', 'Gol', '80000', 200)
print(car.fabricante)
print(car.nome)
print(car.preco)
print(car.potencia)
car.acelerar()
Carro.roncar()

obj = Carro.popular('Ford', 'Fiesta')
print(obj.nome)

atributos = vars(obj)
obj.acelerar()
print(obj.velocity)
obj.velocity = 80
print(obj.velocity)

for chave, valor in atributos.items():
    print(f'{chave}: {valor}')

instancias = [vars(car), obj.__dict__]

def dumpar():
    with open('Classes.json', 'w', encoding='utf8') as fileclass:
        dump(instancias, fileclass, ensure_ascii=False, indent=2)

system('clear')
if __name__ == '__main__':
    dumpar()

