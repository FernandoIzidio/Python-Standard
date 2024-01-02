"""
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
Dunder methods podem ser implementados e modificados em uma classe . Exemplo
Eu posso modificar o metódos __add__ para configurar como se comportaria a operação de soma(metódo), nos objetos de uma classe

-Define como seria a representação grafica em string do objeto
# __repr__(self) - str
- Define a representação gráfica de um objeto
- Também é uma forma de comunicação para outros desenvolvedores, de como objeto deve ser montado
"""

class Cordenadas:
    def __init__(self, x, y, z='String') -> None:
        self.x = x
        self.y = y
        self.z = z

    #Representação gráfica dos objetos da classe Cordenadas e como o objeto deve ser montado
    def __repr__(self) -> str:
        return f'{__class__.__name__}({self.x!r}, {self.y!r}, {self.z!r})'
    
    #Representação string do objeto
    def __str__(self) -> str:
        return 'Objetão'

    def __add__(self, obj):
        atributos = [item for item in vars(self).values()]
        atributos2 = [item for item in vars(obj).values()]
        tupla = []
        if all(isinstance(valor, (int, float)) for valor in atributos) and all(isinstance(valor2, (int, float)) for valor2 in atributos2) and len(atributos) == len(atributos2):
            for pos, valor in enumerate(atributos):
                tupla.append(valor + atributos2[pos])        
        return Cordenadas(*tupla)


cord1 = Cordenadas(8, 7)
print(cord1) #Exibe representação gráfica string de cord1]
print(repr(cord1)) # Exibe como o objeto deve ser montado
print(f'{cord1!r}')

cord2 = Cordenadas(1, 7, 1)
cord1 = Cordenadas(4, 8, 9)
print(repr(cord2.__add__(cord1)))
print(cord1 + cord2)

print(repr(cord2))
