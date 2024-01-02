"""
Se a parent package não for mencionada na importação, ao tentar importar o módulo atual(__init__.py), a partir de módulos externos vai gerar erro, pois os módulos externos não conhecem os módulos internos do caminho atual(sem auxilio da parent package).
"""
from .matematica import *
from .texto import *

printbonito(f'Nome do módulo {__name__}')