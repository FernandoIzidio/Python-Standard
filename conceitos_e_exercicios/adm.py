import subprocess

def admin(password:str, cmd:str):
    senha = password
    comando = cmd  # Substitua "ls" pelo comando que deseja executar com privilégios de administrador

    try:
        proc = subprocess.Popen(['sudo', '-S', comando], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = proc.communicate(input=senha + '\n', timeout=5)
        
        if proc.returncode == 0:
            print("Comando executado com sucesso")
            print("Saída padrão:", stdout)
        else:
            print("Erro ao executar o comando")
            print("Saída de erro:", stderr)

    except subprocess.TimeoutExpired:
        print("Tempo limite expirou")
