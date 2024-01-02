"""
Tipo de dado mutavel, que permite chaves nomeadas para acessar valores

Metódos uteis:
    dicionario.clear - Limpa dicionário
    dicionario.copy - Faz shallow copy do dicionário(copia profunda dos imutaveis, referenciamento dos mutaveis)
    dicionario.fromkeys(iterable, defaultvalue) - Cria um dicionário com as chaves escolhidas, e todas as chaves com valor padrão
    dicionario.keys() - Retorna um iterbla com as chaves do dicionário
    dicionario.values() - Retorna um iterable com os valores do dicionário
    dicionario.items() - Retorna um iterable com chaves e valores do dicionário
    dicionario.get(key) - Retorna um valor de uma chave
    dicionario.pop(key) - Remove chave do dicionário
    dicionaro.popitem() - Remove ultima chave do dicionário
    dicionario.update(kwargs/dict) - Adiciona todas as chaves/valores de um dicionário no dicionário atual
    dicionario.setdefault(key, value) - Retorna valor da chave, e se não encontrar a chave cria a chave com um valor padrão.
"""

dicionario = dict()
truco = dicionario.fromkeys([f'Produto{count}' for count in range(1,11)], 'TRUCOOOOO')
print(truco)
truco.popitem()
print('')
print(truco)
dicionario.update(**truco)
print('')
print(dicionario)
dicionario.setdefault()