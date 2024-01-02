from random import randint
from pandas import DataFrame
import requests

def verifica_alfabeto_latino(palavra: bool):
    return all(ord(letra) < 128 for letra in palavra)

url = f'https://randomuser.me/api/?results={1000}'

# Faz uma requisição e armazena os dados recebidos na variável response
response = requests.get(url)

if response.status_code == 200:

    predados = response.json()
    
    # Pega os valores retornados pela chave results, do dicionário predados
    # Caso não tenha nenhum valor em results, ele vai retornar o valor padrão []
    # para a variável dados
    dados = predados.get('results', [])

    nomesmasc = [{'Nomes': data['name'],
                  'Sexo': 'Masculino',
                  'Endereço': data['address'],
                  'Idade': data['age'],
                  'Celular': data['cell'],
                  'Roupas Compradas': randint(1, 20),
                  'Valor Recebido': f'R${randint(400, 1000) * 2.54:.2f}'.replace('.', ',') 
                  } 
                 for data in
                 list({'name': f'{dicionario["name"]["first"]} {dicionario["name"]["last"]}', 
                       'address': f'{dicionario["location"]["street"]["name"]} n° {dicionario["location"]["street"]["number"]}, {dicionario["location"]["city"]}, {dicionario["location"]["state"]}, {dicionario["location"]["country"]}'
                      ,'cell': f'{dicionario["cell"]}',
                      'age': f'{dicionario["dob"]["age"]} anos'  
                       }
                      for dicionario in dados
                      if dicionario['gender'] == 'male'
                      and (verifica_alfabeto_latino(dicionario['name']['first'])
                           and verifica_alfabeto_latino(dicionario['name']['last'])))]

    nomesfem = [{'Nomes': data['name'],
                 'Sexo': 'Feminino',
                 'Endereço': data['address'],
                 'Idade': data['age'],
                 'Celular': data['cell'],  
                 'Roupas Compradas': randint(1, 20),
                 'Valor Recebido': f'R${randint(400, 1000) * 2.54:.2f}'.replace('.', ',')}
                for data in
                list({'name': f'{datauser["name"]["first"]} {datauser["name"]["last"]}',
                      'address': f'{datauser["location"]["street"]["name"]} n° {datauser["location"]["street"]["number"]}, {datauser["location"]["city"]}, {datauser["location"]["state"]}, {datauser["location"]["country"]}'
                      ,'cell': f'{datauser["cell"]}',
                      'age': f'{datauser["dob"]["age"]} anos'  
                      }
                     for datauser in dados
                     if datauser['gender'] == 'female'
                     and (verifica_alfabeto_latino(datauser['name']['first'])
                     and verifica_alfabeto_latino(datauser['name']['last'])))]
    

    Woman = DataFrame(nomesfem)
    Woman.to_excel('Mulheres.xlsx', index=False)
    Man = DataFrame(nomesmasc)
    Man.to_excel('Homens.xlsx', index=False)
