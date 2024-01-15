"""
__name__ - Nome do módulo
__file__ - Caminho absoluto do arquivo

dump(objeto, json) - Converte um objeto python para json

data = load(json) - Converte um ojbeto json para python

"""
import json
import os


string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

dicionario = json.loads(string_json)

print(dicionario)

caminho, file = os.path.split(__file__)
wayfile = os.path.join(caminho, 'dados.json')

with open(wayfile, 'w', encoding='utf8') as jsonfile:
    json.dump(dicionario, jsonfile, ensure_ascii=False, indent=2)