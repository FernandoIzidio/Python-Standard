from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

    def saudar(self, nome):
        print(f'Bom dia {nome}')



p1 = Pessoa('Carlão', 15)
p1.saudar('Túlio')