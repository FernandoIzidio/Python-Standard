
"""
Threads é um recurso muito util para quando se quer executar multiplos processos/funções ao mesmo tempo, exemplo se vc executar duas funções:

Concorrência - Uma função/tarefa por thread 
Paralelismo - Varias funções sendo executadas ao mesmo tempo

GIL - Global interpreter Lock é um recurso utilizado na implementação do PythonC que impedi que mais de uma thread execute um módulo python ao mesmo tempo, ou seja essa biblioteca só emula threads, porque na pratica é tudo feito em um única thread

fun1()
fun2()

Ambas seguirão o fluxo normal do programa, a fun2 só sera executada após o termino da 1, com threads é possivel executar as duas funções ao mesmo tempo exemplo ilustrativo:

correr() e atirar()

A função correr e atirar sera executada ao mesmo tempo


Criação de threads:

    Por classes - a classe deve herdar da classe threads , e implementar no run todos os processos que serão executados na thread, cada instância dessa classe sera uma thread

    Por funções = usa-se a classe t1 = thread(target=function, args=()) - a classe thread executara essa função com estes argumentos

Metódos de objetos threads:
    t1.start() - Inicia/executa uma thread em parelelo com o main
    t1.is_alive() -> bool - Verifica se a thread ainda esta em execução
    t1.join() - Coloca uma thread no fluxo normal do programa, ou seja, outra função só vai ser executada quando a thread acabar


Lock:
    objeto.acquire() -> Garante que uma função/metódo só permita ser executada por  uma thread por vez

    objeto.release() -> Destranca e libera o metódo para ser executado por outras threads



"""
from threading import Thread, Lock
from functools import partial
from time import sleep
import threading



class Process(Thread):
    def __init__(self, func,time,  *args) -> None:
        self.func = func
        self.args = args
        self.time = time
        super().__init__()

    def run(self):
        sleep(self.time)
        self.func(*self.args)


def correr(time):
    while True:
        if time <= 0:
            break
        
        print("Correndo", time)
        sleep(1)
        time -= 1



def atirar(time):
    while True:
        if time <= 0:
            break
        
        print("Atirando", time)
        sleep(1)
        time -= 1
        


p1 = Process(correr, 3, 10)
p1.start()
p2 = Process(atirar, 1, 10)
p2.start()

