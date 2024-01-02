"""
Váriaveis de ambiente são variaveis do sistema operacional temporarias, que permanecem no so até o fechamento do terminal.

São especialmente uteis para melhorar a segurança de um código, e para proteger as senhas dos usuários em variaveis de ambiente

dotenv:
    load_dotenv() - Carrega as variaveis de ambiente de um arquivo .env

os.environ - Retorna as variaveis de ambiente do SO
os.getenv(var) - Retorna o valor de uma variavel de ambiente
os.putenv(name, value) - Cria uma variavel de ambiente
os.unsetenv(var) -Remove variaveis de ambiente
 
Ao criar programas com variaveis de ambiente, é preciso indicar para outros desenvolvedores, também criarem um arquivo de variavel de ambiente

Outro forma de criar variaveis de ambiente é com os

os.environ["nomevar"] = "valor" cria uma variavel de ambiente  
ou
os.putenv(name, value)


.gitignore - é usado para ignorar arquivos, e fazer que determinado arquivos não subam pro github

dir env: - Retorna variaveis de ambiente SO

É preiciso criar um arquivo .env-example, indicando para outros desenvolvedores todas as variaveis que precisam ser criadas

"""
import dotenv #type: ignore
import os

dotenv.load_dotenv() #Carrega variaveis de arquivo .env do diretório atual
print(os.getenv('SENHA1')) # Retorna valor dessas variaveis
print(*os.environ)