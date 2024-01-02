from contextlib import contextmanager

#Esse decorator vai implementar os metódos e atributos necessários para se ter um context_manager personalizado
@contextmanager
def My_Context_Manager(wayfile, mode):
    try:
        print('__Enter__: Abrindo o arquivo')
        file = open(wayfile, mode, encoding='utf8')
        print('Retornando conteúdo do arquivo para variável depois do as')
        yield file
        print('Conteúdo retornado, e context manager despausado')
    except Exception as error:
        print('Exit: Ocorreu um erro.')
        print(f'ERROR: {error}')
    finally:
        print('Fechando arquivo')
        file.close()


Cm = My_Context_Manager('decoratorcontextfile.txt', 'w')

with Cm as datafile:
    datafile.write('Primeira linha do arquivo.txt\nEm um arquivo criado por context manager de decorator')
    datafile.write(2, 4)
