from pathlib import Path
import os
import sys
currentdir = Path(__file__).parent

os.chdir(currentdir)
sys.path.append(currentdir)
from . import controle_de_processos, documentation, formatatamanho, function_walk, os_e_shuti_funcs, os_path, os_stat_objects