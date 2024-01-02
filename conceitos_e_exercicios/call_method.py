"""
__call__ - Faz um objeto de uma classe ser callable

-callable é que pode ser chamado com parenteses objeto()
"""

from typing import Any

class telefone:
    def __init__(self, nome) -> None:
        self.nome = nome

    def __str__(self) -> str:
        return 'Objetão'
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({vars(self)})'
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return 'Flamengo piada'
    


obj = telefone('Flachacota') 

print(obj.nome)
print(obj)
print(repr(obj))
print(obj())