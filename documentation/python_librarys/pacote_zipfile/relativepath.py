"""
caminho relativo funciona como cd!
ele mostra oque é preciso escrever para acessar determinado arquivo diretorio, a partir do diretorio atual

obj.path(way) - Retorna o caminho relativo pra acessar obj, a partir de way

"""


from pathlib import Path

# Defina os caminhos absolutos dos diretórios ou arquivos
dir1 = Path(__file__)
dir2 = Path(__file__).parent 
print(dir1)
print(dir2)
# Calcule o caminho relativo de dir1 para entrar em dir 2
caminho_relativo = dir1.relative_to(dir2)

print(f'Caminho relativo: {caminho_relativo}')
