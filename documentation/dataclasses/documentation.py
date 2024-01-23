
"""
Dataclasses recurso que facilita muito a criação de novas classes, pois vem com muitos metódos e atributos implementados

quando o decorator dataclass é chamado antes da hora, é possivel definir quais metódos ele vai ter implementado ou não

Toda dataclasse precisa de tipagem

funções do modulo dataclasses:
    dataclass - Decorator utilizado para modificar uma classe para dataclasse
    astuple - Converter uma instância de uma dataclasse em tupla
    asdict -  Converter um objeto de uma dataclasse em dict(dataclasses não suportam vars())
    field - Configura atributos de dataclasses
    fields(fieldSets) - Mostra todas as configurações de um atributo


field :
    Default_Factory/Default - chama/executação função/classe do valor padrão, caso não seja fornecido nenhum valor
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

