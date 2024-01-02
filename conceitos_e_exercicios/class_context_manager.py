"""
É possivel implementar qualquer protocolo de forma personalizada, apenas definindo/implementando os metódos(metódos e dunder methods) e atributos que compõem esse protocolo

Isso é chamado de duck typing um conceito relacionado com tipagem dinamica, onde o python não está interessado no tipo, mas sim na presença dos metódos e atributos que compõem o tipo


Criar uma classe para gerenciar contextos permite maior liberdade, controle e personalização que a extrutura with open.
-Permite maior personalização ao poder customizar/modificar os metódos que compõem a extrutura with open

Para criar um context manager, os metodos __enter__ e __exit__ devem ser implementados


O metódo __init__ recebe o caminho do arquivo, e o modo de abertura

O metódo __enter__ é responsável por retornar o conteúdo do arquivo, para a variável depois do as
-Além de retornar o contéudo do arquivo para a variavel depois do as, ele também é o responsável por abrir o arquivo


O metódo __exit__ vai receber a classe de exceção, a exceção e o traceback
-Se ele retornar True, ele vai suprimir a exceção que ocorrer em with

Recebe o nome e caminho do arquvio

"""

class My_open_Manager:
    def __init__(self,wayfile, mode) -> None:
        self.wayfile = wayfile
        self.mode = mode
        self.__datafile = None

    #Representação string do objeto
    def __str__(self) -> str:
        return 'Objetão'
    
    #Representação de como o objeto deve ser montado
    def __repr__(self) -> str:
        return f'{__class__.__name__}()'

    #Retorna o contéudo do arquivo para variavel depois do as
    def __enter__(self):
        print('Enter')
        self.__datafile = open(self.wayfile, self.mode, encoding='utf8')
        return self.__datafile

    #Recebe a classe da exceção, a exceção e o traceback
    def __exit__(self, classexception_, msgexception_, traceback_):
        print('Exit')
        self.__datafile.close()
        #raise classexception_(*msgexception_.args).with_traceback(traceback_)
        print(classexception_)
        print(msgexception_)
        print(traceback_)
        #python 3.11 suporta notas na mensagem de erro
        #msgexception_.add_note('Ocorreu um erro')

        return True

#Objeto instaciado/inicializado e herdou os atributos e metódos da classe File_Manager, e definiu o valor de seus atributos
Fm = My_open_Manager('magicfile.txt', 'w')

with Fm as fileman:
    print(f'With: {Fm}')
    fileman.write('First line, with a personal context_manager, maked by class manipulation')
    fileman.write(131, 154)
    print(f'Conteúdo: {fileman}')
    print(f'Montagem de objeto: {Fm!r}')

