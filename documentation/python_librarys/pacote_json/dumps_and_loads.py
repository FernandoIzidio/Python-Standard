
"""
dumps(objpython) -> String - Resumindo mostra a representação string de um obj python no formato json
iterable = loads(string) - Converte a representação string de um objeto json, para um objeto python
"""
from typing import TypedDict
import json


class Dados(TypedDict):
    nome: str
    sobrenome :str
    idade : int
    solteiro : None  

string: Dados= '''
{"nome": "Tulio",
"sobrenome": "Pneu",
"idade": 65,
"solteiro": null
}
'''
iterable: dict = json.loads(string)
print(iterable)
print('Objeto python, conertido em Stringjson:')
objjson = json.dumps(iterable, indent=False, ensure_ascii=False)
print(objjson)



