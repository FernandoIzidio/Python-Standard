"""
path(__file__).parent / 'arquivo.txt'
/ -> Indica uma concatenação da string ao caminho absoluto
__file__ -> passa o caminho do módulo atual como argumento
.parent -> O atributo parent retorna o caminho absoluto do módulo atual
"""


from pathlib import Path

logfile = Path(__file__).parent / 'Teste.txt'

print(logfile)
