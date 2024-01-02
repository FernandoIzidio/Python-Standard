
"""
Dataclasses é um decorator que facilita a criação de novos classes, por vir com metódos e atributos já implementados

quando a dataclasse é chamada antes da hora, é possivel definir quais metódos ele vai ter ou não

Toda dataclasse precisa de tipagem

astuple - Permite converter um objeto de uma dataclasse em tupla
asdict - Permite converter um objeto de uma dataclasse em dict(dataclasses não suportam vars())
fields - Mostra todas as configurações de um atributo

field - Permite definir um valor padrão mutavel ou imutavel  para um atributo de uma dataclasse, e definir o comportamento desse atributo, se o atributo vai ser incluido no __init__, __repr__, calculo do hash, como variavel a mais na determinação de igualdade e etc

field :
    Default- Valor padrão do atributo caso não seja fornecido
    Default_Factory - chama/executação função/classe do valor padrão, caso não seja fornecido nenhum valor
    repr - define se o atributo vai ser incluido no repr
    compare - Define se o atributo vai ser incluido no comparations
    hash - Define se o atributo vai ser incluido no calculo do hash

"""
from dataclasses import dataclass, astuple, asdict, field
from faker import Faker
database = Faker()
@dataclass(frozen=True)#Implementa metódo frozen
class Pessoas:

    nome: str = field(default_factory= lambda: database.name())
    idade: int = field(default_factory= lambda: database.random_int(1, 99))
    sexo: str = field(default_factory= lambda:database.random_elements(elements=('Masculino', 'Feminino')))
    tel:int = field(default_factory=lambda: f'({database.random_int(11,99)}){database.random_int(9000, 9999)}-{database.random_int(11111, 99999)}', repr=False, compare=False)


for count in range(5):
    obj = Pessoas()
    print(*vars(obj).items(), sep='\n')
    print(repr(obj))
del obj

