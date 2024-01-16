
"""
Módulo excelente para execução de processos ou comandos externos ao python
Ele só executa processos e programas que podem ser executados por terminal

stdout -> saida de dados do processo
stdin -> entrada de dados do processo
stderr -> Redirecionam os erros do processo

capture_output - Captura erros que ocorrorem para criar log, ou captura apenas qualquer saida do programa

text - Se true as entradas e saidas vão ser tratadas como texto na codificação utf-8
shell - Se true o processo tera acesso ao shell do sistema
returncode - 0 processo executado com sucesso, caso contrario não executou o processo
127.0.0.1

stdout - Retorna dados de saida de um processo, em bytes
"""
import subprocess, locale

cmd = ['ping', '127.0.0.1']
process = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=locale.getencoding(), 
)

print(process.stdout)