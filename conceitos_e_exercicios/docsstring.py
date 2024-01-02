import d_aux_string

"""
dir(modulo)
Retorna a parent class, as docsstrings, __file__ caminho do arquivo, __name__ nome do módulo

tudo que está entre três aspas sãos docsstrings

help(modulo) - retorna  nome do módulo, dados, e docstrings
"""

print(dir(d_aux_string))

print(d_aux_string.__doc__)
print(d_aux_string.__file__)
print(d_aux_string.__name__)
print(d_aux_string.__package__)
help(d_aux_string)