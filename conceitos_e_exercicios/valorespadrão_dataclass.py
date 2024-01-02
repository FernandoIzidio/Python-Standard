"""
Apenas atributos imutaveis podem receber valores padrões em dataclasses

Mas com o field default_factory é possivel atribuir valor padrão a atributos imutaveis

asdict == vars == obj.__dict__

field:
    default_factory = class
    chama uma classe e cria um obj para um parametro mutavel

    default = valor
    define um valor padrão para objeto imutavel

"""

from dataclasses import field, dataclass, asdict, astuple

@dataclass
class Cliente:
    nome: str = field(default='Truco')
    idade: str = 'Desconhecida'
    renda: float = 'Variável'
    enderecos: list = field(default_factory=list)


obj = Cliente()
print(asdict(obj))
print(vars(obj))
print(astuple(obj))




