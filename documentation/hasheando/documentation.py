
"""
Hash é um valor único que identifica um objeto

Objetos hasheaveis podem ser usados como chaves de dicionário

hash() aceitam apenas valores imutaveis como argumentos, ou seja apenas valores imutaveis são hashaveis
Dois objetos iguais e como mesmo valor de conteúdo retornam o mesmo hash(identificador único), dependendo da implementação do metódo equal

__hash__ - Permite que instâncias da classe sejam usadas como chaves de dicionário

__hash__ atua em conjunto com __eq__
"""
from faker import Faker
randomdata = Faker()
class Registro:
    def __init__(self, nome:str, sexo:str, idade:int, email:str) -> None:
        self.nome = nome
        self.user = f'{nome.replace(" ", "_")}{randomdata.random_int(min=0, max=1000)}' 
        self.sexo = sexo
        self.idade = idade
        self.email = email

    def __str__(self) -> str:
        return self.user

    def __eq__(self, other: object) -> bool:
        if self.email == other.email and isinstance(other, Registro):
            return True
        return False
    

    def __hash__(self) -> int:
        return hash(self.email)



database = set()

for count in range(8):
    database.add(Registro(randomdata.name(), randomdata.random_elements(elements=('Masculino', 'Feminino')), randomdata.random_int(min=0, max=99), randomdata.email()))


