from classes_e_objetos import Carro
from json import load
with open('Classes.json', 'r', encoding='utf8') as fileclass:
    dics = load(fileclass)


carro1 = Carro(*dics[0].values())
carro2 = Carro(*dics[1].values())
dupla = [carro1.__dict__, vars(carro2)]
for dicionario in dupla:
    for valor in dicionario.values():
        print(valor)