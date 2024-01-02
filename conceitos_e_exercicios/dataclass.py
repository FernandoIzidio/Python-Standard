"""
São decorators que ajudam/facilitam na criação de metódos e atributos para outras classes
O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
post_init__ init após a criação de um objeto, util para atrbuir atributos no escopo do objeto
dataclass(init= false)
Obriga a implementar o metódo __init__

"""

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split(' ')
        sobrenome = ' '.join(sobrenome)
        self.nome = nome
        self.sobrenome = sobrenome


if __name__ == '__main__':
    obj = Pessoa('Tulio', 'André', 45)
    obj2 = Pessoa('Tulio', 'Tiago',45)
    print(obj.nome)
    print(obj.idade)
    print(obj)
    print(obj == obj2)
    print(obj.nome_completo)
    print(obj2.nome_completo)
    obj2.nome_completo = 'Seu Bené Augusto'
    print(obj2.nome_completo)