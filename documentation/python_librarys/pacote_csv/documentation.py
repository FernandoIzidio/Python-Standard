"""
 CSV (Comma Separated Values - Valores separados por vírgulas)

É um formato de arquivo que armazena dados em forma de tabela, onde cada linha representa uma linha da tabela e as colunas são separadas por vírgulas.

Ele é amplamente utilizado para transferir dados entre sistemas de diferentes plataformas, como por exemplo, para importar ou exportar dados para uma planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.

Transferência de dados, assim com json e xml


Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
editor de texto ou em uma planilha eletrônica.

Um exemplo de um arquivo CSV pode ser:

Nome,Idade,Endereço
Luiz Otávio,32,"Av Brasil, 21, Centro"
João da Silva,55,"Rua 22, 44, Nova Era"

A primeira linha do arquivo define os nomes das colunas da, enquanto as
linhas seguintes contêm os valores das linhas, separados por vírgulas.
Regras simples do CSV

1 - Separe cada coluna com um delimitador único (,)
2 - Cada registro deve estar em uma linha
3 - Não deixar linhas ou espaços sobrando
4 - Use o caractere de escape (") quando o delimitador aparecer no valor.

csv:
    reader() - Retorna um iterator de listas com todas as linhas do arquivo csv

    DictReader() - Retorna uma iterator de dicionarios, onde cada dicionário é uma linha do arquivo csv

    writer(wayfile) - Cria um objeto escritor para escrever sobre o arquivo csv

        wt.writerow - Escreve uma linha no arquivo


    DictWriter(fileopen, fieldnames=[colunas]) - Retorna objeto escritor para escrever em arquivo csv

"""
from pathlib import Path
import csv, faker
from random import randint
currentdir = Path(__file__).parent
fk = faker.Faker("pt_BR")

clientes = ({"Nome": f"{fk.name_male()}",
            "Idade": f"{fk.random.randint(16, 80)}",
            "Endereço": f"{fk.address()}".replace('\n', ""),
            "Telefone": f"{fk.phone_number()}",
            "Email": f"{fk.safe_email()}"
            } for count in range(10))
#Generator

with open(currentdir / "dados_clintes.csv", 'w', encoding="utf-8") as csvfile:
    escritor = csv.writer(csvfile)
    data = next(clientes)
    escritor.writerow(data.keys())
    escritor.writerow(data.values())
    for client in clientes:
        escritor.writerow(client.values())


with open(currentdir / "dados_clintes.csv", 'r', encoding="utf") as csvfile2:
    content = csv.reader(csvfile2)
    for row in content:
        print(row)