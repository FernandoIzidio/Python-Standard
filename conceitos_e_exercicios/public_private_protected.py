"""
Public - Pode ser usado em qualquer trecho do código

_Protected_- Só deve ser utilizado na parent class e child class's

__Private__ - Só deve ser utilizado na parent class
"""

class Acesso:
    def __init__(self) -> None:
        self.public = 'Acesso Público'
        self._protected = 'Acesso Protegido'
        self.__private = 'Acesso Privado'

    def publico(self):
        return 'Metódo de ' + self.public
    
    def _protegido(self):
        return 'Metódo de ' + self._protected
    
    def __privado(self):
        return 'Metódo de '+ self.__private
    


key = Acesso()
print(key.public)
print(key._protected)
print(key._Acesso__private)
print('')
print(key.publico())
print(key._protegido())
print(key._Acesso__privado())
