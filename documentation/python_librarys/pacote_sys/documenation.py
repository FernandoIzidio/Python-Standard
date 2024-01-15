
"""
sys é o melhor modulo para interagir com o interpretador, execução de módulos, argumentos para script python, e configurações de ambiente python

sys.argv - Retorna os argumentos passados na execução de um script, o primeiro argumento sempre vai ser caminho/nome do módulo.

sys.platform - Retorna a plataforma que está executando o módulo atual

sys.path - Define de quais caminhos um módulo pode importar, é util para manipulação de importação

sys.flags - Permissões do módulo atual

sys.modules() - Retorna os módulos importados pelo módulo atual

sys.exit() - Encerra a execução de um módulo python

sys.version() - Versão do python

sys.gc() - Faz coleta de lixo manualmente

sys.stdin - É a referência de todas as entradas de dados do script

sys.stdout - Referência de todas as saidas do script, pode ser usado para redirecionar saidas de script apra arquivos de log em especifico

stdout, stdin, stderror:
    .write('msg') - Escreve uma mensagem em algum dos buffers

    .flush() - Esvazia buffer de entrada, saida ou erro, e imprime mensagem no terminal ou arquivo imediatamente, ao invés de esperar que o programa esvazie o buffer automaticamente

sys.sterror - Usado para redirecionar erros do script.

sys.getsizeof(obj) - Retorna o tamanho em bytes, de um objeto python

sys.getrecursionlimit() - Retorna o limite de recursão do módulo atual

sys.setrecursionlimit() - Define o limite de recursão

sys.getfilesystemencoding() - Retorna a codificação do sistema de arquivos atual

sys.getdefaultencoding() - Retorna a codificação usada pelo interpretador

sys.getrefcount(object) - Retorna o número de referências para determinado objeto

sys.hash_info - Fornece informações sobre calculo de hash utilizado em dicionarios e listas

sys.getwindowsversion() - Retorna objeto com informações sobre a versão versão do windows

sys.get_int_max_str_digits - Retorna o limite de conversão de str em int
    sys.set_int_max_str_digits - Define o limite de conversão de str em int

"""
import sys, os
os.chdir(os.path.dirname(__file__))
print(sys.modules.keys())

print(sys.get_int_max_str_digits())

filesystem_encoding = sys.getfilesystemencoding()
print(filesystem_encoding)


print('BLA')



listaorigin = ["TEDAS"]
listcopy1 = listaorigin

listcopy2 = listaorigin
listcopy3 = listaorigin
listcopy4 = listaorigin

#         LISTA
#       /       \
# reforiginal  [ref1, ref2, ref3, ref4, reffunc]

print(sys.getrefcount(listaorigin)) #Passando referência da lista para a função

class ContextManager:
   def __init__(self, path, mode, logpath, modelog) -> None:
      self.path = path
      self.mode = mode
      self.logpath = logpath
      self.modelog = modelog
      self.originstate = sys.stderr
    
   def __enter__(self):
      sys.stderr = open(self.logpath, self.modelog)
      

      self.file_descriptor = open(self.path, self.mode)
      sys.stdout = self.file_descriptor #Redirecionando todas as saidas de dados do programa para o conteúdo desse filedescriptor
      
      return self.file_descriptor


   def __exit__(self, clserror, msgerror, traceback):
      self.file_descriptor.close()      
       

with ContextManager('output.txt', 'w', 'log.txt', 'w') as file:
   print('Bla2')
   print('BLA4')
   
   raise NotImplementedError from TimeoutError


   