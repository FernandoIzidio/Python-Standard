#Python 3.11.0
class OptionError(Exception):
    ...

def raisingerror():
    obj = OptionError('Selecione uma opção válida.', 'Flapiada')
    obj.add_note('Nota de erro')
    raise obj

class ERRO2(Exception):
    ...

try:
    raisingerror()
except OptionError as msgerror:
    print(msgerror.args)
    obj2 =ERRO2('Flapiada')
    raise obj2 from msgerror