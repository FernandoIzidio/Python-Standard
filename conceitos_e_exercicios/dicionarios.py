"""
Extrutura de dados iteravel, com as seguintes caracteristicas:
- São mutaveis, podem receber novos valores, e remover valores
-Tem indíces nomeados

Metódos importantes:
.items() - Retorna chave e valores de um dicionário
.values() - Retorna apenas valores de um dicionário
.keys() - Retorna Apenas chaves de um dicionário
.pop(key) - Remove chave e valor do dicionario
.popitem() - Remove o ultimo item(chave/valor) do dicionário
.copy() - Retorna Shallow copy do dicionário
.setdefault(chave, default) - Retorna o valor de uma chave do dicionário, e se chave não existir ele cria a chave como valor default, e retorna o valor dessa dessa chave criada
.get(chave, padrão) - Retorna o valor de uma chave e se a chave não existir ele retorna o valor padrão escolhido pelo usuário
.update(dic/chave = valor) - Adiciona as chaves valores de um dicionário a outro dicionário, também pode receber novas chaves e valores com chave = valor, ou pode ser usado para atualizar chaves e valores antigos
.fromkeys([keys], padrão) - Retorna um novo dicionário com as chaves escolhidas tendo um valor padrão
.sort(key) - Ordena um dicionário de acordo com a chave escolhida
""" 
from random import randint
dicionario = {f'Nome {cont+1}': f'Produto {cont+1}'  for cont in range(10)}

dicionario.pop('Nome 10')
print(dicionario)
print(dicionario.setdefault('Nome 8'))
print(dicionario.get('Chave fake', 'Não tem chave'))
print(dicionario.setdefault('Chave criada', 'Valor gerado'))
print(dicionario['Chave criada'])
newdic = dicionario.fromkeys(['Nome 1','Nome 2','Nome 3'], f'R${randint(20,100) * 2.54:.2f}'.replace('.', ','))
print(newdic)
 