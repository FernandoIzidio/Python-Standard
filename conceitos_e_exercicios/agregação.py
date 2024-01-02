"""
Agregação - Relação média entre classes, é quando uma classe precisa da outra para executar um metódo
Um carro pode existir sem roda, e uma roda sem carro, mas um carro não pode correr sem a roda
"""
from functools import reduce
from random import randint
class Carrinho:
     def __init__(self) -> None:
            self.__produtos = []
     
     def inserir_produto(self, *produtos):
          for produto in produtos:
               self.__produtos.append(produto)
     
     def remover_produto(self):
            self.refazer = []
            if self.__produtos:
                 self.refazer.append(self.__produtos[-1])
                 self.__produtos.pop()
            self.listar()

     def refazer_produto(self):
          if self.refazer:
               self.__produtos.append(self.refazer[-1])
               self.refazer.pop()
          self.listar()
          
     def total(self):
          tot = reduce(lambda acumulador, item: acumulador + item.preco, self.__produtos, 0)
          print(f'Total gasto: {tot}')  
     
     def listar(self):
          print('')
          for produto in self.__produtos:
               print(produto.nome, f'R${round(produto.preco * 1.141, 2)}'.replace('.', ','), produto.quantidade, sep=' ||| ')

    
class Produtos:
     def __init__(self, nome, preco, quantidade) -> None:
          self.nome = nome
          self.quantidade = quantidade
          self.preco = preco * quantidade
     
     @classmethod
     def compra_rapida(cls, nome):
          temp = cls(nome, randint(5, 20), randint(30, 100))
          return temp


kart = Carrinho()

for count in range(20):
    temp = Produtos.compra_rapida(f'Laticionio {count+1}')     
    kart.inserir_produto(temp)

kart.listar()
kart.remover_produto()
kart.inserir_produto(Produtos.compra_rapida('Carne'))
kart.refazer_produto()
kart.total()

