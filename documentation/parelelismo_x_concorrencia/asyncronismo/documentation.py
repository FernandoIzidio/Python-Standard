"""

funções asyncronas são uteis quando se é nessário executar multiplas tarefas ao mesmo tempo, sem travar a aplicação até determinada tarefa terminar

aiohttp - Lib para fazer requisições asyncronas
requests - Lib para fazer requisições sincronas

Uma expressão asyncrona(promisse e etc) - É todo objeto que possui o dunder method __await__

funções asyncronas seguem essa extrutura

async def Name():
    await - Pausa execução da função e aguarda promisse/função async ser resolvida
    do anything...

Asyncio - Usado para tratar de funções asyncronas no python de forma mais concisa

    asyncio.run(foo()) - Executa uma função asyncrona
    asyncion.gather(foo(), foo2()) - Executa várias funções em parelelo
    await asyncio.wait_for(minha_funcao_assincrona(), timeout=2) - Atrasar execução de funções asyncronas
    loop = asyncio.get_event_loop()
    loop.run_until_complete() - pausa a execução do código até a função asyncrona ser resolvida


Loop de eventos é um mecanismo que espera o acontecimento de eventos para retornar respostas/tarefas a esses eventos. Ele gerencia  a ordem em que as tarefas/respostas são executadas, com base nos eventos disponiveis

"""
import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete()