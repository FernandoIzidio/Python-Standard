"""
Gera números pseudo aleatórios a partir dos milisegundos do computador, é um pacote util quando não se precisa de segurança na criação de números aleatórios, como criptografia

random:
    randint(init, stop) -> int - Retorna um número aleatório nesse intervalo
    randrange(init, stop, step)-> int - Funciona como um intervalo range, mas para gerar números inteiros aleatórios com mais parametros

    uniform(init, stop) -> float - Retorna um número de tipo float no intervalo informado

    shuffle(iterable) -> iterable - Embaralha uma sequence/iterable

    choice(iterable) -> value/any - Retorna um valor aleatório dentro de uma lista/iterable


    sample(iterable, k/quantidade_items=item) -> iterable - Gera uma amostra de valores aleatórios baseado em uma lista

    choices(iterable, k=int) -> iterable - Faz a mesma coisa que o sample, mas pode ter valores repetidos


    seed(value) - Inicializado de objeto aleatório random, é util modificalo, quando se precisa fazer resultados previsiveis de forma aleotória, é bastante util para testes. 

"""
import random

