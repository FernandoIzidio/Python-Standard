from collections.abc import Iterable, Sized
from typing import Iterator


class Numeric(int, Iterable):
    def __init__(self, valor) -> None:
        super().__init__()
        self.valor:int = valor
        self.nextind = 0
        self.len = len(str(self.valor))

    def __len__(self):
        return self.len
    
    def __getitem__(self, ind):
        valor = str(self.valor)
        return int(valor[ind])

    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self):
        if self.nextind >= self.len:
            raise StopIteration
        
        algarismo = str(self.valor)[self.nextind]
        self.nextind += 1
        return int(algarismo)
    
    
obj = Numeric(501)


for pos, alg in enumerate(obj):
    print(alg)
    print('=')
    print((alg+1) * 2)
    print('-')
    
