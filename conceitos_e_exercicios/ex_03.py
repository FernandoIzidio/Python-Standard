"""


"""
from os import system
from time import sleep
class Fabricante:
    def __init__(self, nome:str) -> None:
        self.__nome = nome
        self.__carros = []

    
    @property
    def nome(self):
        return self.__nome

    @property
    def carros(self):
        return self.__carros


    def inserir_carro(self, nome, ano, preco, tipo):
        self.__carros.append(Carro(nome, ano, preco, tipo))

    def mostrar_carros(self):
        print(f'Marca: {self.nome}')
        for carro in self.__carros:
            mostrarattr(carro)
            print('')
    


class Carro:
    def __init__(self, nome:str, ano:int, preco:float,tipo:str) -> None:
        self.__nome = nome
        self.__ano = ano
        self.__tipo = tipo
        self.__preco = preco
        self.__motor = None

    def setmotor(self, obj):
        self.__motor = obj

    def checkvelocidade(self):
        if self.__motor:
            self.velocidade = ((0.10 * self.__motor.potencia)* 3.6) + 10
            print(f'Velocidade atual do {self.nome}: {self.velocidade}.')
        else:
            print('Não tem motor')

    @property
    def preco(self):
        return self.__preco

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano
    
    @property
    def tipo(self):
        return self.__tipo
    


class Motor:
    def __init__(self, marca:str, potencia:int) -> None:
        self.marca= marca
        self.potencia= potencia


def mostrarattr(obj, retorno = False):
    atributos = {chave.replace('_', ' ').strip().split(' ')[-1].capitalize(): valor for chave, valor in vars(obj).items()}
    if not retorno:
        print('='*50)
        for chave, valor in atributos.items():
            print(f'{chave}: {valor}' if not isinstance(valor, Motor) and chave != 'Preco' else f'{chave}: {valor.marca}' if chave != 'Preco' else f'{chave}: {f"R${valor:.2f}"}'.replace('.', ','))
        print('='*50)
    else:
        return atributos

def fast(fab, objcar):
    fab.inserir_carro(**{chave.lower(): valor for chave, valor in mostrarattr(objcar, True).items() if chave != 'Motor'})

motor1 = Motor('Classic', 160)
motor2 = Motor('Strong', 240)

lan = Carro('Lancer Evolution', 2023, 350000,'Esportivo')
lan.setmotor(motor2)
mostrarattr(lan)
print('')

paj = Carro('Pajero', 2021, 280000,'Hibrido')
mostrarattr(paj)
print('')

fie = Carro('Fiesta', 2022, 180000,'Popular')
fie.setmotor(motor1)
mostrarattr(fie)

input('Next: ')
sleep(2)
system('clear')
Mit = Fabricante('Mitsubshi')
Ford = Fabricante('Ford')

fast(Mit, lan)
fast(Mit, paj)
fast(Ford, fie)

Mit.mostrar_carros()
input('Next: ')
sleep(2)
system('clear')
Ford.mostrar_carros()


for carro in Mit.carros:
    carro.setmotor(motor1)
    carro.checkvelocidade()

for carro in Ford.carros:
    carro.setmotor(motor2)
    carro.checkvelocidade()



Mit.mostrar_carros()
input('Next: ')
sleep(2)
system('clear')
Ford.mostrar_carros()