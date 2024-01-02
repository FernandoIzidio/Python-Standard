# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
#Init também é responsável por herdar os atributos do objeto, e atribuir valor aos atributos do objeto
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        print('Antes de criar o objeto na parent class(object)')
        instancia = super().__new__(cls)
        print('Antes de retornar o objeto')
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'


b = object.__new__(A)
print(b.magic)
b.__init__(8)
print(b.x)
a = A(123)
print(a.x)
