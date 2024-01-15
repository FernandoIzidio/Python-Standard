"""
Váriaveis de ambiente são variaveis do sistema operacional temporarias, que permanecem no so até o fechamento do terminal/encerramento de processo.

São especialmente uteis para melhorar a segurança de um código, e para proteger as senhas dos usuários em variaveis de ambiente

dotenv:
    load_dotenv(file=".env") - Carrega as variaveis de ambiente de um arquivo .env, e implementa esses variaveis de ambiente no processo atual

    dotenv_values(file=".env") - Funciona de forma semelhante ao load_dotenv(), porém ao inves de implementar variaveis de ambiente, apenas pega variaveis de ambiente de arquivo em especifico e converte pra dict

    dotenv.set_key('file', key, value) - Define o valor de uma variavel de ambiente de arquivo .env

    dotenv.get_key('file', key) - Retorna o valor de uma varivel de ambiente em de arquivo em especifico


Ao criar programas com variaveis de ambiente, é preciso indicar para outros desenvolvedores, também criarem um arquivo de variavel de ambiente



É preiciso criar um arquivo .env-example, indicando para outros desenvolvedores todas as variaveis que precisam ser criadas

"""
import dotenv #type: ignore
import os
os.chdir(os.path.dirname(__file__))

dotenv.load_dotenv() #Carrega variaveis de arquivo .env do diretório atual
print(os.getenv('SENHA1')) # Retorna valor dessas variaveis
print(*os.environ)
print('\n\n\n')
print(dotenv.set_key('.env', 'SENHA2', 'bla2'))
print(os.getenv('SENHA2'))
print(dotenv.get_key('.env',"SENHA3"))
print(dotenv.dotenv_values())