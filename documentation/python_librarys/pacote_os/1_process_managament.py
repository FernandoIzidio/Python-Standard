
"""
Filedescriptor - Número inteiro que identifica um processo em execução

CHDIR - Change directory, usado para mudar diretório de trabalho atual
FCHDIR - Change directory basead in file descriptor - Muda o diretório de trabalho somente durante a execução do filedescriptor.

OctPermitionMask - É um número octal que concede permissões a determinadas a  processo no SO

Sistema de arquivos - NTFS, etx4, FAT32

grupo de processos - É um grupo de processos distintos ou semelhantes, que mantém uma relação entre si, e são tratados de forma coletiva pelo SO. Ou seja quando eu quero agrupar um conjunto de processos que se comuniquem o ideal é definir um gpid

ID Real - Permissões reais no momneto de execução do processo

ID efetivo - Permissões temporarias validas apenas durante a execução do processo.

ID saved - Permissões efetivas que foram persistidas para posteriores execuções desse processo.

Conjunto de funções de OS que são usadas para identificar processos em execução, arquivos abertos, configurar permissões, definir mascaras e etc:

    name - Nome do SO em execução, posix, nt, java

    os.uname() - Retorna informações que identificam o sistema operacional atual, versão, arquitetura, e id de rede

    os.kill(pid, signal) - Emite signals para o sistema operacional em determinado processo, SIGKILL é um signal bem comum para encerrar um processo

    environ - Retorna variaveis de ambiente do SO

    environb - Retorna variaveis de ambiente do SO no formato binário

    getenv - Retorna o valor de uma variavel de ambiente

    getenvb - Retorna o valor de uma variavel de ambiente no formato binário
    
    os.putenv(key, value) - Define variavel de ambiente
    
    os.unsetenv(key, /) - Remove variavel de ambiente no processo atual



    os.open(way, maskoctal, * , permitions) -> filedescriptor - Abre um arquivo/processo, com determinadas permissões

    os.close(fd) - Encerra um processo em execução

    
    os.getcwd() - Retorna o diretório de trabalho atual

    os.chdir(caminho:str) - Define o diretório de trabalho atual

    os.fchdir(fd) - Define o diretório de trabalho atual somente para um processo em execução

    

    fsencode(caminho:str) -> str - Codifica um caminho para a codificação do sistema de arquivos atual

    fsdecode(bytes) -> str - Decodifica um sequência de bytes que representam um caminho, para o formato str

    fspath(caminho: str | bytes) -> str | bytes - Retorna determinado caminho em um formato compativel com o sistema de arquivos atual

    
    os.get_exec_path() - Retorna uma lista de diretórios, os quais o sistema busca por arquivos executaveis. São esses caminhos que o módulo subprocess procura, ao trabalhar com executaveis  

    os.geteuid - Retorna o id de usuário efetivo do processo atual, ou seja retorna o id do usuário que está executando o processo.

    os.getegid - Retorna o id do grupo efetivo do processo atual, ou seja o id do grupo que está executando o processo

    os.getuid - Retorna o id real do usuário atual

    os.getgid - Retorna o id real do grupo atual

    os.getgrouplist - Retorna uma lista de id's dos grupos, que usuário pertence

    os.getgroups - Retorna uma lista de id's dos grupos, que o processo atual pertence

    os.getlogin - Retorna o nome do usuário que está logado no terminal 

    os.getpgid(pid) - Retorna o id do grupo de processos, que o processo especificado pertence, se pid for 0 ele retorna o id do grupo de processos, do processo atual

    os.getpid() - Retorna o id do processo atual
    
    os.getpgrp() - Retorna o id do grupo de processos, do processo atual

    os.getppid - Retorna o id do processo pai do processo atual

    os.getpriority(Prio_, id) - Retorna o nivel de prioridadde de um processo, grupo de processos ou de um usuário:
        PRIO_PROCESS, pid - Retorna o nível de prioridade um processo baseado no seu id
        PRIO_PGRP, pgid - Retorna o nivel de prioridade de um grupo de processos
        PRIO_USER, uid - Retorna o nivel de prioridade de um usuário

    
    os.getresuid() - Retorna o id de usuário real, efetivo(executando o processo) e salvo

    os.getresgid() - Retorna o id de grupo de usuário real, efetivo(grupo que ta executando o processo) e salvo

    os.initgroups(username, gid) - Usado para definir os grupos de um processo, ou seja definir quais usuários fazem parte de quais grupos, em determinados processos(software em execução)

    os.setegid(egid, /) - Define o id de grupo efetivo para o processo atual

    os.seteuid(euid, /) - Define o id de usuario efetivo para o processo atual

    os.setgid(gid) - Define o id de grupo real para o processo atual

    os.setgroups(groups) - Define a lista de grupos que o processo atual pertence, ou seja define quais grupos de usuário controlam o processo

    os.setpgrp() - Define de qual grupo de processos, o processo atual faz parte

    os.setpgid(pid, pgrp) - Define o id do grupo de processos atual

    os.setpriority(PRIO_, ID, prioritylevel:int) -  Define o nivel de prioridade de um processo, grupo de processos, usuario
    
    os.setregid(rgid, egid, /) - Define o id de grupo efetivo e real para o processo atual

    os.setresgid(rgid, egid, sgid, /) - Define o id de grupo salvo, efetivo(que está executando o processo) e real para o processo atual

    os.setreuid(ruid, euid, /) - Define o user id efetivo e real para o processo atual

    os.setresuid(ruid, euid, suid, /) - Define o user id salvo, efetivo, e real para o processo atual


    os.getsid(pid, /) -Retorna a sessão do grupo de processos atual

    os.setsid(uid) - Define qual a sessão que vai controlar e ter permissões no processo atual

    os.strerror(code) - Retorna a mensagem de erro correspondente ao código de erro

    os.supports_bytes_environ - Verifica se as variaveis de ambiente podem ter valor bytes

    os.umask(mask) - Define a mascara de usuario para o processo atual

  
    
    
    """
import os, os.path as path
import psutil

currentprocess = psutil.Process(os.getpid())

print(*os.get_exec_path(), sep='\n')
print("Usuário logado no terminal: ",os.getlogin())
print("Id do processo atual: ", os.getpid())
print("Id do pai do processo atual", os.getppid())
print("Nome do processo: ", currentprocess.name())
print("Nome do pai do processo: ", psutil.Process(os.getppid()).name())
print("Status do processo: ",  psutil.Process(os.getpid()).status())
print()
print("Value in Bytes for Vars Envirotment:", os.supports_bytes_environ)
print(os.access('C:\\', mode=os.O_RDONLY))

os