"""
O módulo principal(atualmente em execução) tem nome __main__

Os módulos importados tem o próprio nome do módulo

atributo/várivel sys.path:
mostra o caminho do modulo atual
e o caminho de suas depedências
path também mostra de qual caminhos os módulos podem ser importados


para importar módulos fora caminho atual, é preciso manipular sys.path
"""
import mpart2
import sys 
sys.path.append('/home/pennpc')
try:
    import foravenv    
except ModuleNotFoundError:
    print('Módulo não encontrado')

print('O módulo atual é o:', __name__)
print('')
print('')
print(f'lista dos caminhos do arquivo: \n{sys.path}')
print('')
print('')
print(f'Caminho absoluto do arquivo e suas depedências:', end='')
print(*sys.path, sep='\n')

import my_package as modulo #My package passa e se comportar como módulo por causa do init, ai é possível importar classes, funções e variaveis de mypackage
from my_package import matematica
from my_package.matematica import multiplicar as multi
from my_package import printbonito
from my_package.texto import printbonito as printao


modulo.texto.printbonito(str(modulo.multiplicar(8, 9)))
printbonito(str(multi(8, 7)))
printao(str(matematica.dividir(8, 4)))

