
"""
Dunder Methods - Responsaveis por definir todas as operações suportadas por um objeto python

hash(object) - Retorna um hash único de um objeto
~object - Invente cada bit de um objeto, 0 vai ser invertido para 1, e 1 invertido para 0
object2^object - Realiza xor operation em cada bit dos objetos, a xor operation, retorna o bit 1, se a correspondência dos bits for diferente, e 0 se forem iguais
__instancecheck__(self, instance) - Define o comportamento da função isistance(), e checa se uma instância objeto pertence a classe atual de acordo com as condições definidas, é esperado que esse dunder method retorne bool

__subclasscheck__(self, subclass) - Define o comportamento da função issubclass(), ou seja define sobre quais condições uma outra classe é filha da atual 

methods of construction and inicialization:
    - __new__(cls, *args) - Responsável por criar um objeto/classe
    - __init__ - Responsavel por inicilizar objeto e atribuir atributos ao objeto
    - __del__ - Define o comportamento de remoção de um objeto
    - __call__ - Torna um objeto callable
    

Representation Methods:

    __repr__ - Define como um objeto deve ser montado
    __str__ - Define a representação string de um objeto
    __bool__ - Define o valor boolean de um objeto
    __format__(self, formatos) - Define os tipos de formatação suportados por um objeto, uma formatação é definida pelo valor depois dos : exemplo objeto:format, é possivel customizar a representação de um objeto de acordo com um formato escolhido
    __hash__ - Define o hash único dos objetos da classe, ao implementar esse dunder method, os objetos da classe podem ser usados como chaves de dicionário. Define o comportamento da função hash() no objeto da classe
    __dir__ - Define o comportamento da função dir(), e deve retornar uma dicionário de atributos e metódos do objeto
    __dict__ - Define o comportametno da função vars(), e deve retornar uma dicionário de atributos do objeto
    __sizeof__ - Define o comportametno da função sys.getsizeof()


Comparations Methods:
    __eq__(self, other) - Defines behavior for the equality operator, ==.
    __ne__(self, other) -Defines behavior for the inequality operator, !=.
    __lt__(self, other) - Defines behavior for the less-than operator, <.
    __gt__(self, other) - Defines behavior for the greater-than operator, >.
    __le__(self, other) - Defines behavior for the less-than-or-equal-to operator, <=.
    __ge__(self, other) - Defines behavior for the greater-than-or-equal-to operator, >=.
    __contains__(self, other) - Define o comportamento da operador in, ou seja determina sobre quais condições um outro objeto vai estar dentro do objeto atual


Numeric Methods:
    __pos__ - Define a versão positiva do objeto
    __neg__ - Define a versão negativa do objeto
    __abs__ - Define o valor absoluto do objeto, e o comportamento para função abs()
    __invert__ - Define o comportamento do operador de operador de inversão bit a bit ~, 
    __round__ - Implementa o comportamento de arredondamento da função round()
    __floor__ - Define o comportamento da função floor()
    __ceil__ - Define o comportamento da função ceil()
    __trunc__ - Define o comportamento da função trunc(), e deve retornar a versão inteira do objeto

arithmetic operators:
    __add__(self, other) - Implementa cOMPORTAMENTO DO operador de +
    __sub__(self, other) - Implementa COMPORTAMENTO DO operador de -
    __mul__(self, other) - Implementa COMPORTAMENTO DO operador de *
    __floordiv__(self, other) - Implementa comportamento DO operador da divisão inteira,  //
    __truediv__(self, other) - Implementa comportamento do operador de divisão /
    __mod__(self, other) - Implementa comportamento do operador %
    __pow__ - Implementa comportamento do operador de potenciação **
    __divmod__(self, other) - Implementa comportamento da função divmod()
    __lshift__(self, other) - Implementa comportamento do operador de deslocamento a esquerda <<
    __rshift__(self, other) - Implementa comportamento do operador de descolamento a direita >>, adiciona 0 as esquerda dos bits, cada deslocamento equivale a uma divasão por 2
    __and__(self, other) - Implementa comportamento do operador &, deve realizar operação bit and bit entre os objetos passados
    __or__(self, other) - Implementa comportamento do operador |, deve realizar uma operação bit or bit, entre os objetos passados
    __xor__(self, other) - Implementa comportamento do operador bit a bit ^

    
reflected arithmetic operators:
    objeto + main = operação refletida, define o comportamento de quando o objeto está sofrendo uma operação, ou sendo usado como objeto secundário em uma operação


    __radd__(self, other) - Implements reflected addition.
    __rsub__(self, other) - Implements reflected subtraction.
    __rmul__(self, other) - Implements reflected multiplication.
    __rfloordiv__(self, other) - Implements reflected integer division using the // operator.
    __rtruediv__(self, other) - Implements reflected true division. Note that this only works when from __future__ -  Mostra imcompatiblidades da linguagem atualmente
    __rmod__(self, other) - Implements reflected modulo using the % operator.
    __rdivmod__(self, other) - Implements behavior for long division using the divmod() built in function, when divmod(other, self) is called.
    __rpow__ - Implements behavior for reflected exponents using the ** operator. here the mainobject is the pow raised
    __rlshift__(self, other) - Implements reflected left bitwise shift using the << operator.
    __rrshift__(self, other) -Implements reflected right bitwise shift using the >> operator.
    __rand__(self, other) -Implements reflected bitwise and using the & operator.
    __ror__(self, other) - Implements reflected bitwise or using the | operator.
    __rxor__(self, other) - Implements reflected bitwise xor using the ^ operator.

Metódos atribuição + operador:
    __iadd__(self, other) - Implements behavior  of addition with assignment. +=
    __isub__(self, other) - Implements behavior of subtraction with assignment. -=
    __imul__(self, other) - Implements behavior of multiplication with assignment. *=
    __ifloordiv__(self, other) - Implements behavior of integer division with assignment. //=
    __itruediv__(self, other) - Implements true division with assignment. /=
    __imod__(self, other) - Implements behavior of modulo with assignment.  %=
    __ipow__ - Implements behavior for exponents with assignment using the **= operator.
    __ilshift__(self, other) - Implements behavior left bitwise shift with assignment. <<= 
    __irshift__(self, other) - Implements behavior right bitwise shift with assignment. >>=
    __iand__(self, other) - Implements behavior bitwise and with assignment. &=
    __ior__(self, other) - Implements behavior bitwise or with assignment. |= 
    __ixor__(self, other) - Implements bitwise xor with assignment. ^= 
           
Conversion Methods:
    __int__ - Define o comportamento de conversão para inteiro do objeto. a classe int() usa esse metódo para criar um objeto da classe inteiro
    __float__ - Define o comportamento da classe float() no objeto atual
    __complex__ - Define o comportamento da classe complex()
    __oct__ - Define o comportamento da função oct() no objeto atual
    __hex__ - Define o comoportamento da função hex() no objeto atual

    
Controle de acesso:
    __getattr__(self,name) - Define o comportamento se for digitado um atributo inexistente no objeto
    __setattr__(self, name) - Define o comportamento de alteração/criação de atributos em um objeto
    __delattr__(self, name) - Define o comportamento de remoção de atributos em um objeto
    __getattribute__(self, name) - Toda vez que um atributo é chamado/usado, esse metódo é executado.

    
Sequencesmethods:
    __len__ - Define o comportamento da função len()
    __getitem__(self, key) - Torna um objeto fatiavel, e permite acessar valores do objeto por chaves
    __setitem__(self, key, value) - Permite alterar valores de fatias/partes/itens do objeto
    __delitem__ - Permite deletar fatias/partes/ itens do objeto
    __iter__ - torna um objeto iteravel, e deve retornar o próprio objeto self 
    __next__ - Define o comportamento da função next() no objeto, e permite que chama próximos valores em um objeto, ou seja transforma um objeto em um iterator, um iterator deve mostrar o próximo valor, e retornar um erro stop iteration para parar a iteração de um for                                              
    
    __reversed__ - define o comportamento da função reversed()
    __missing__ - Define o comportamento caso for digitado uma chave errada.
"""
