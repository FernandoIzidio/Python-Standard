from functools import reduce, partial
from typing import Callable, Iterable

class Cobaias:
    def __init__(self, valor:str) -> None:
        self.valor:str = valor.upper()
        self.letras:str = ''.join([letra for letra in self.valor if letra.isalpha()])
        self.numeros: int = int(''.join([letra for letra in self.valor if letra != self.letras and letra]))

    def __add__(self, other):
        if self.letras == other.letras:
            soma = self.numeros + other.numeros
            return Cobaias(f'{soma} {self.letras}')

    def __eq__(self, __value: object) -> bool:
        if self.letras == __value.letras:
            return True
        else:
            return False

    def __str__(self) -> str:
        return self.valor
    
    def __repr__(self) -> str:
        return self.valor
    

cobaia = list(Cobaias(input()) for count in range(int(input())))
somacobaias: Callable = partial(reduce, lambda acum, obj: obj.numeros + acum)
somatotal = somacobaias(cobaia, 0)
tracklist: Callable = lambda key: somacobaias([cob for cob in cobaia if key in repr(cob)], 0)
coelhos, ratos, sapos = tracklist('C'), tracklist('R'), tracklist('S')

print(f"""Total: {somatotal} cobaias
Total de coelhos: {coelhos}
Total de ratos: {ratos}
Total de sapos: {sapos}
Percentual de coelhos: {((coelhos / somatotal)*100):.2f} %
Percentual de ratos: {((ratos / somatotal)*100):.2f} %
Percentual de sapos: {((sapos / somatotal)*100):.2f} %""")