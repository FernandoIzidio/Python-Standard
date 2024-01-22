"""
argparse - É um argv mais robusto, ou seja argumentos de script de forma mais robusta. É usado para intepretar argumentos de módulo python, muito util para criação de script cli


argparse recebe uma chave de argumento e o valor do argumento ex:
python3 __name__.py arg1 value arg2 value

parser = ArgumentParser() - Cria um parser para interpretar argumentos do módulo atual


obj.add_argument(-name) adiciona um argumento reconhecido pelo módulo

args = obj.parse_args() - Interpreta os argumentos passados pelo interpretador

    args.get_kwargs() -> dict.items() - Retorna as chaves e valores dos argumentos do script
    args.get_args() -> list - Retorna os valores de argumentos recebidos

argscript.add_argument(-nome, 
        --explicação(VERSÃO VERBOSA), 
        help='oque o arg de script faz', 
        type=class Define o tipo do arg,
        default=any Define o valor padrão do argumento, caso não seja fornecido
        metavar- Documentação do argumento
        action- func: 
                    append - lista de argumentos
                    store_true - Verifica se a var de script recebeu algum argumento/valor
                    
        -> Indica uma ação a ser executado quando o argumento é recebido
        nargs - int -> Determina o número máximo de args a receber)
        required - bool -> Define a obrigatoriedade de passar o arg
"""
from argparse import ArgumentParser

argscript = ArgumentParser()

argscript.add_argument('-m', '--msg', help='Set the message to send', type=str, metavar='string', default='Hello World')

argscript.add_argument('-c', '--copy', 
                       help='Set the number of "Msg\'s" in return terminal',
                       type=int,
                       metavar='int',
                       default=1)



args = argscript.parse_args()

for count in range(args.copy):
    print(args.msg)