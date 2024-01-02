
"""
Dataclass são decorators que permitem criar metódos e atributos de classe de uma forma muito otimizada, mas também permitem liberdade na hora da criação das classes por meio de config

dataclass(init=False)

Cria a necessidade de implementar init

dataclass(frozen=True)

Deixa os objeto de uma classe congelados, ou seja não podem ser alterados


dataclass(order)
ordeno os objetos de uma classe pelo valor dos parametros
"""

from dataclasses import dataclass


@dataclass(init=False)
class Pessoas:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split(' ')
        sobrenome = ' '.join(sobrenome)
        self.nome = nome
        self.sobrenome = sobrenome


print(Pessoas('Tulio', 'Pneu').nome_completo)

obj = Pessoas('Seu', 'Bené')
print(obj)
print(obj.nome_completo)
obj.nome_completo = 'Tulio Pneu Silvestre Mago'
print(obj.nome_completo)
print(obj.sobrenome)

@dataclass(frozen=True)
class Dinheiro:
    Quantidade: int
    Valor: float = 1


br =  Dinheiro(500, 3)
print(br.Quantidade)
print(br.Valor)
