
"""
Convenções:
    self - usado para se referir objetos, ou metódos e atributos de objeto
    cls - class
    mcs - metaclasse


metaclasse - object - classe - objeto

type(classname, herança, atributosdaclasse)

Type Checker - É um verificador de tipos em python, o typechecker usado pelo vscode é mypy

Erro Import Circular o módulo1 importa o módulo2, e o módulo2 importa o módulo1

Type Checking:
    typing.TYPE_CHECKING - Se o módulo estiver em execução(main), a variavel retorna False, caso contrário retorna True
    Para importar módulos apenas para checagem, usa-se a flag TYPE_CHECKING, para importar os módulos de tipagem, e com as classes importadas, na tipagem a classe tem que estar entre aspas exemplo:
        'class'


eval(pythonexprresion:str) -> Any - eval é uma função que vai interpretar a representação em string de uma expressão python, vai executar essa expressão e retornar o resultado dessa expressão,

@overload Permite que uma classe seja instaciada de mais de uma maneira, ou seja a classe vai poder ser instaciada de varias formas e com varios __init__
-Ter varios __init__(forma de iniciliazar um objeto), permite maior flexibilidade e variação na hora de instaciar um objeto, ou seja, é possivel definir varios tipos de caracteristicas inicializadas por padrão para um objeto

obj = object.__new__(classe) - Cria um novo objeto par auma classe.
obj.__init__() - Inicializa o objeto e atribui seus atributos

pythonw - Python Window, pode ser usado para executar módulos de forma desaclopada do terminal, pythonw
abre um processo, para executar o módulo

.pyi - É um arquivo de tipagem python

ducktyping - O python não está interessado nos nomes das classes, o python está interessado mais na presença de determinados metódos ou atributos

Sobreposição = Suportado pelo python, só é possivel implementar/modificar metódos e atributos em um objeto/classe, se a parent class possuir os mesmos.
Sobrecarga - Qualquer metódo/atributo pode ser implementado em qualquer objeto/classe, independente desses metódos existirem ou não na parent class

mro() - Method resolution order - o python sempre vai buscar os metódos na child class primeiro dps nas parent class

__name__ - nome do modulo atual
    __name__ == "__main__" - Módulo em execução

__file__ - Caminho absoluto do módulo atual
__docs__ - Doscstrings e comentários de um módulo

__new__ - cria e retorna objeto/classe
__init__ - inicializa objeto e atribui atributos ao objeto


super() - Retorna objeto da parent class
super().method() - Executa um metódo na parent class

Pilares da POO:
    -Herança: Um objeto/classe pode herdar todos os metódos e atributos de uma outra classe
    -Encapsulamento: Controle de acesso, public, _protected disponivel apenas para parent class e child class, __private disponivel apenas para a parent class
    -Polimorfismo: duas childs class que herdam de uma mesma parent class podem ter metódos e atributos de mesma assinatura, mas que se comportam de maneira diferente.
    -Abstração - Extrair metódos e atributos importantes para um objeto, ou definir a assinatura de todos os metódos e atributos em uma parent class, a classe abstrata não pode ser instanciada diretamente e para ter acesso aos metódos e atributos da parent class, é preciso implemnta-los na child class


decorator - Função/classe que modifica outra função/classe, pode retornar o objeto/classe que modifica ou substitui-lo.
closure - Função que retorna função



Metódos:
    @classmethod: cria um metódo de classe, para combinar com outros decorators este tem que ser o mais externo

    @property/getter - Metódos que se comportam como atributos
    
    @setter - Permite alterar o valor de um atributo property, para implementar um setter, primeiro é preciso ter uma property implementada

    @staticmethod - Não tem acesso ao objeto nem a classe

    @abstractclassmethod - Cria um metódo abstrato, que proibe que uma classe(abstrata) seja instaciada diretamente, para ter acesso a esse metódo abstrato é preciso implentalo em uma child class, deve ser usado como decorator mais interno ao combinar com outros decorators

    
    
yield - pausa a execução de uma função e retorna um valor, permite usar next(function) na função
nonlocal function/var - Permite modificar um função ou var de um escopo mais externo, mesmo estando em um escopo mais interno


    """

