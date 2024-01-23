"""
Pickle é um módulo muito util para serializar objetos, classes e funções python em um formato binário, para poder armazenar estado de aplicações, ou transmitir por rede dados entre sistemas que utilizem python


Dados serializados por pickle só podem ser deserializados por python
"""
import pickle
from random import uniform
from pathlib import Path

currentway = Path(__file__).parent

produtos =  [{f"Produto {count}": f'R${count*uniform(2, 5):.2f}'.replace('.', ',')} for count in range(1, 10)]
purebinary = pickle.dumps(produtos)
print(purebinary)

print('')

with open(currentway / 'dados.pkl', 'wb') as datafile:
    pickle.dump(produtos, datafile)


dataconverted = pickle.loads(purebinary)
print(dataconverted)

with open(currentway / 'dados.pkl', 'rb') as datafile:
    print()
    dados = pickle.load(datafile)
    print(dados)