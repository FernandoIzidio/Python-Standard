"""
stat - retorna um objeto com status/perfil completo de um arquivo

tempo epoch ==  timestamp

stmode -  Verifica as permissões do arquivo, e o tipo do arquivo(diretório, arquivo, atalho)
stino - Retorna o númeero inode(número identificador exclusivo no sistema de arquivos) PRIMARY KEY
dtdev - Retorna o endereço do dispositivo fisico em que o arquivo  esta armazenado
st_nlink - Retorna o número de referências/atalhos para o arquivo 
st_uid - Retorna o id do usuário
st_gid - Retorna o id do grupo
st_atime - Retorna o timestamp da ultima vez que o arquivo foi lido
st_mtime - Retorna o timestamp da ultima vez que o arquivo foi modificado
st_ctime - Retorna o timestamp do ultima mudança de status/permissões
st_blksize - Retorna tamanho utilizado para alocação do arquivo
st_blocks - Retorna o números de blocks(padrão 512 bytes cada bloco), que determinado arquivo ocupa


"""
import sys, os, datetime, math

waydir, filename = os.path.split(os.path.abspath(__file__))
numberofdirs = os.stat(os.path.join(waydir,  "texto.txt")).st_nlink
os.chdir(waydir)
print(os.getcwd())

def format_size(tamanho_em_bytes: int, base: int = 1024) -> str:
    if tamanho_em_bytes <= 0:
        return "0B"
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    potencia = base ** indice_abreviacao_tamanhos
    tamanho_final = tamanho_em_bytes / potencia
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


perfil = os.stat('texto.txt')
print("Nível de permissão: ", perfil.st_mode)
print("Identificador: ", perfil.st_ino)
print("Endereço de Dispositivo:", perfil.st_dev)
print("Nº de diretórios: ", numberofdirs)
print("Id user: ", perfil.st_uid)
print("ID Group: ", perfil.st_gid)
print("Tamanho: ", format_size(perfil.st_size))
print("Ultima leitura: ", datetime.datetime.fromtimestamp(perfil.st_atime).strftime("%d/%m/%Y %H:%M:%S"))
print("Ultima modificação: ", datetime.datetime.fromtimestamp(perfil.st_mtime).strftime("%d/%m/%Y %H:%M:%S"))
print("Data de criação: ", datetime.datetime.fromtimestamp(perfil.st_ctime).strftime("%d/%m/%Y %H:%M:%S"))
