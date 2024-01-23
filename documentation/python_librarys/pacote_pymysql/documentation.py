"""
Pymysql é um pacote utilizado para fazer conexão do python com o banco de dados

instalação:
    pip install pymysql
    pip install types-pymysql

conn = pymysql.connect(host="localhost", user="", password="", "port")  Cria uma conexão com um data base em especifico
cursor = conn.cursor() - Retorna um cursor para manipular o banco de dados, e executar querys


conn.commit() - Confirma as alterações realizadas durante uma conexão
cursor.close() - Fecha o cursor
conn.close()- fecha as conexões

cursor.fetchone() - Recupera um registro capturado por uma query
cursor.fetchall() - Recupera todos registros capturados por uma query

%(dict_key)s - Placeholder utilizado para inserção de valores, em consultas parametrizadas

cursor.execute(query, parameters) - Executa uma query no db
cursor.executemany(query, parameters) - Executa a mesma query, até o determinado número de parametros

cursor.mogrify(query, parameters) -> str - Retorna a query SQL sem executar ela, vai retornar a query parametrizada, conforme executada pela banco de dados.

cursor.scroll(pos, "absolute") - Retorna o número de pos, de registros recuperados pra trás, e permite recuperar registros novamente com fetch, e absolute determina a a posição que os arquivos não recuperados vão começar a recuperar a partir de todos os registros capturados por uma query

%s - placeholder trata qualquer valor que receber como valor, e e previne de SQLInjection

pymysql.cursor - É um módulo que contém varias classes de cursores(para manipular DB), cada classe de cursor vai retornar um tipo de dado em especifico, o dictcursor retorna dicionarios quando se recupera registros, já o cursor padrão retorna tuplas
pymysql.rownumber - Retorna a linha atual do cursor

typing cast, faz a conversão de tipos

SSUnbefered, quando os registros são recuperados, retorna um generator que vai retornar cada registro recuperado.
Não tem como fazer scroll em SSBD

"""
import pymysql
from pprint import pprint

conn = pymysql.connect(**{
    'host': "localhost",
    'user': "usuario",
    'password': "senha",
    "port": 3306
})

cursor = conn.cursor()

cursor.execute('SHOW DATABASES;')

def get_database_tables(dbname: str) -> list:
    """
    This function is used to fetch all tables in a Database

    Parameters:
        dbname: str
            Name of database
    Returns:
        list
    """

    cursor.execute(f"USE {dbname};")
    cursor.execute(f"SHOW TABLES;")
    tables = [table_tp[0] for table_tp in cursor.fetchall()]
    return tables


def update_current_db(dbname: str) -> None:
    cursor.execute(f"USE {dbname}")


databases = cursor.fetchall()
databases = {tuple_db[0]: get_database_tables(tuple_db[0]) for tuple_db in databases if tuple_db[0] not in ["performance_schema", "information_schema"]}


update_current_db("Enterprise")
cursor.execute(f"DESCRIBE {databases.get('Enterprise')[0]}")
print(cursor.fetchall())