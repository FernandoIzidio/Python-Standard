"""
Composição - Quando o ciclo de vida de uma classe depende de outra classe
Ou seja quando há um obj de outra classe, na parent class
Ciclo de vida INTERDEPENDENTE
"""

from os import system
from time import sleep
class Carros:
        def __init__(self, marca, nome, preco, ano):
            self.marca = marca
            self.nome= nome
            self.preco = preco
            self.ano = ano
            self.motor = Motores(self.marca, 220)
            self.velocidade = ((self.motor.potencia * 0.10) * 3.6) + 20

        def acelerar(self):
            while True:
                 print(f'Velocidade: {round(self.velocidade)}')
                 cmd = input('Acelerando, digite stop quando quiser parar:').capitalize()
                 match cmd:
                      case 'Stop':
                           print('Carro estacionado com sucesso')
                           break
                      case _:
                           print('BRUUUUUUUUUUUM BRUM BRUM BRUM')
                           self.velocidade += (0.05 * self.motor.potencia)
                
                 if self.velocidade > 240:
                      print('SE FUDEU!!!!!')
                      print('O carro desviou da pista e bateu.')
                      print('Digirir não é brinquedo')
                      break
                 sleep(1)
                 system('clear')
class Motores:
     def __init__(self, modelo, potencia) -> None:
        self.modelo = modelo 
        self.potencia= potencia
     
     def colocaroleo(self):
          print(f'Colocando um óleo no motor da {self.modelo}')

mit = Carros('Mitsubshi', 'Lancer Evolution', 250000, 2023)
print('='*50)
for chave, valor in vars(mit).items():
     print(f'{chave}: {valor}' if not isinstance(valor, Motores) else
           f'{chave}: {valor.modelo}')
print('='*50)
mit.motor.colocaroleo()
print('Preparando para corrida')
print('3, 2, 1 ...')
mit.acelerar()