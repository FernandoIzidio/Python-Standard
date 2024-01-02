"""
Módulos padrão do Python (import, from, as e *)

Inteiro: 
import nome_modulo
import sys
-Vantagens: você tem o namespace do módulo
-Desvantagens: nomes grandes


Partes(Importar funções ou classes do módulo) 
from nome_modulo import objeto1, objeto2
from sys import exit, platform

-Vantagens: nomes pequenos
-Desvantagens: Sem o namespace do módulo

--As(muda nome de pacote, módulo, função)
- import nome_modulo as apelido
import sys as s
from nome_modulo import objeto as apelido

- Vantagens: você pode reservar nomes para seu código
- Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo(funções, classes, variaveis e etc)
# Desvantagens: importa tudo de um módulo
# Só pode ser utilizado no módulo __init__.py de um pacote, para importar todos os outros módulos
"""