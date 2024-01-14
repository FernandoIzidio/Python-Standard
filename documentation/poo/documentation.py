
"""
Convenções:
    self - usado para se referir objetos, ou metódos e atributos de objeto
    cls - class
    mcs - metaclasse

ducktyping - O python não está interessado nos nomes das classes, o python está interessado mais na presença de determinados metódos ou atributos

GIL - Global interpreter Lock a implementação do python padrão em C, tem esse esse recurso GIL, que permite que apenas uma thread por vez execute um módulo python

Toda classe tem que ser reutilizavel em diversos contextos, para solucionar um problema em especifico

Interfaces - São um conjunto de metódos que uma child-class que herda dessa interface pode implementar
Obs: Não é possivel implementar nenhum metódo concreto em uma interface.

Em classes abstratas, além de definir a assinatura de uma familía de classes. É possivel ter metódos abstratos/metódos de assinatura(para serem implementados nas childs class), e metódos concretos. Ou seja classes abstratas tem tanto metódos de assinatura, como metódos concretos.

obs: Nas interfaces só é possível implementar metódos de assinatura.

S - Single reponsability princible - Toda função/metódo tem que ter apenas uma responsabilidade.
O - Open to extend/Close to modify Princible - Toda class é aberta  a ser extendida e fechada para modificações
L - Liskov Copy Princible - Toda child class tem que ser capaz de substituir a parent class, sem quebrar o programa
I - Interface Segregation Princible - Não forçar uma classe a implementar interfaces/classes abstratas, que não são relevantes para a classe. Segregar classes abstratas e interfaces, e deixar a child class, escolher qual classe abstrata/interface implementar
D - Dependecie Inversion Princible - Principio da inversão de dependência, a parent class/class abstrata não deve depender da child class. E sim a child class tem que depender da parent class/classe abstrata


transpilador - Converte código de uma linguagem para outra

interpretador - Um interpretador analisa o código fonte, e compila/transpila o código fonte, em uma linguagem de baixo nivel ou bytecode, o interpretador da linguagem vai interpretar essa linguagem de baixo nivel, ou esse bytecode, e executar cada comando linha a linha

ByteCode - Nivel intermediario entre linguagem e código de maquina, não varia de acordo com a arquitetura, e pode ser interpretado independente da plataforma.

JIT(Just in Time) - Se refere ao processo de compilação em código de maquina, apenas durante a execução do programa.

O pyhton ao executar gera um arquivo bytecode pyc, que vai ser interpretado pelo interpretador PythonC, que vai compilar linha a linha, cada linha do bytecode em código de maquina.

Compilador - Compilador analisa o código fonte inteiro e gera um arquivo executavel, com código de maquina

Para otimizar a execucação de scripts o python compila o código python em bytecode arquivo.pyc, que é um intermediario entre linguagem de programação e linguagem de máquina, pyc é um arquivo gerado automaticamente para otimizar a excução de um módulo python


Sobreposição = Suportado pelo python, só é possivel implementar/modificar metódos e atributos em um objeto/classe, se a parent class possuir os mesmos.

Sobrecarga - Qualquer metódo/atributo pode ser implementado em qualquer objeto/classe, independente desses metódos existirem ou não na parent class


CPython: É o interpretador padrão python.

Jython: Um interpretador Python que roda na Máquina Virtual Java (JVM).

IronPython: Um interpretador Python que roda no ambiente .NET.

PyPy: Um interpretador alternativo que visa ser mais rápido do que o CPython. Ele usa a compilação just-in-time (JIT) para otimizar o desempenho. Este interpretador, converte linha a linha no momento de execução, cada linha em código de maquina, sem passar pelo processo de compilação em bytecode. Oque melhora muito o desempenho. Esse interpretador é mais utilizado em jogos

MicroPython: Projetado para ser executado em ambientes com recursos limitados, como microcontroladores.

Stackless Python: Uma versão modificada do CPython que adiciona suporte para microthreads.

Todo metódo por padrão tem acesso aos objetos da classe, ou seja todo metódo por padrão é metódo de objeto

Exceto o metódo __new__ que sempre sera metódo de classe(cls, mcs), reponsável por gerar instâncias da classe, ou classes da metaclasse
    
metaclasse(type) - object - classe - objeto

type(classname, herança, atributosdaclasse)

Type Checker - É um verificador de tipos em python, o typechecker usado pelo vscode é mypy

Erro Import Circular o módulo1 importa o módulo2, e o módulo2 importa o módulo1

.pyi - É um arquivo de tipagem python

pythonw - Python Window, pode ser usado para executar módulos de forma desaclopada do terminal, pythonw
abre um processo, para executar o módulo

Type Checking:
    typing.TYPE_CHECKING - Se o módulo estiver em execução(main), a variavel retorna False, caso contrário retorna True
    Para importar módulos apenas para checagem, usa-se a flag TYPE_CHECKING, para importar os módulos de tipagem, e com as classes importadas, na tipagem a classe tem que estar entre aspas exemplo:
        
        'class'

__name__ - Módulo em execução 


eval(pythonexprresion:str) -> Any - eval é uma função que vai interpretar a representação em string de uma expressão python, vai executar essa expressão e retornar o resultado dessa expressão,

@overload 
function/method/class
Vai definir as varios tipos os quais uma classe, function ou method pode ser chamado


obj = object.__new__(classe) - Cria um novo objeto para auma classe.
obj.__init__() - Inicializa o objeto e atribui seus atributos


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

    -Encapsulamento: Controle de acesso:
        public - Disponivel em todo o código
        _protected - disponivel apenas para parent class e child class
        __private - disponivel apenas para a parent class

    -Polimorfismo: duas childs class que herdam de uma mesma parent class podem ter metódos e atributos de mesma assinatura, mas que se comportam de maneira diferente.

    -Abstração - Extrair metódos e atributos importantes para um objeto, ou definir a assinatura de todos os metódos e atributos em uma parent class, a classe abstrata não pode ser instanciada diretamente. E para ter acesso aos metódos e atributos da parent class, é preciso implemnta-los na child class. Classes abstratas são classes de assinatura


decorator - Função/classe que modifica/substitui outra função/classe, pode retornar o objeto/classe que modifica ou substitui-lo.

closure - Função que retorna função
callback - Função que vai ser chamada em cada elemneto de um array




Metódos:
    @classmethod: cria um metódo de classe, para combinar com outros decorators este tem que ser o mais externo

    @property/getter - Metódos que se comportam como atributos
    
    @setter - Permite alterar o valor de um atributo property, para implementar um setter, primeiro é preciso ter uma property implementada

    @staticmethod - Não tem acesso ao objeto nem a classe nem ao objeto, é apenas um metódo protegido pelo escopo da classe

    @abstractclassmethod - Cria um metódo abstrato, que proibe que uma classe(abstrata) seja instaciada diretamente, para ter acesso a esse metódo abstrato é preciso implentalo em uma child class, deve ser usado como decorator mais interno ao combinar com outros decorators

    
    
yield - pausa a execução de uma função e retorna um valor, permite usar next(function) na função, é usado para criar generators

generators são tipo extrutura de dados, que só mostram os próximos valores

Deque - É uma extrutura de dados onde cada elemento só conhece o proximo valor e valor anterior, é uma extrutura mais otimizada que a lista

nonlocal function/var - Permite modificar um função ou var de um escopo mais externo, mesmo estando em um escopo mais interno


function* name(){
    yield "";
}; - Generator function(extrutura de dados que só mostra o próximo valor)

    """

