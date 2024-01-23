"""
GIL (Global Interpreter Lock): Python possui o GIL, que permite que apenas uma thread execute código Python puro por vez. Isso significa que, embora você possa usar threads para executar tarefas de E/S simultaneamente (como leitura/gravação de arquivos ou comunicação de rede), as threads não são eficazes para paralelizar cálculos intensivos de CPU em Python.


Concorrência : É um conceito onde uma unica atividade é dedicada a um único nucleo/thread, ou seja um o nucleo vai executar uma unica tarefa, é possivel selecionar qual thread/núcleo vai executar determinada tarefa. A biblioteca que vai cuidar disso é threads.

Threads permitem executar multiplos processos/módulos ao mesmo tempo


"""