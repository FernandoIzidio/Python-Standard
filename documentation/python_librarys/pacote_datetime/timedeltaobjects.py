"""
Objetos timedelta representam a diferença entre dois objetos time e date, ou dois objetos datetime

TimeDelta é o descolamento de tempo

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) - Para criar um objeto timedelta, todos argumentos de construção são opcionais, e os argumentos podem receber valores inteiros, ou flutuantes

se o objeto timedelta receber argumentos para minutes, miliseconds, hours, weeks, eles serão convertidos, em days, seconds, e microseconds internamente, e todas valores fracionarios são arredondas para inteiro internamente

Atributos de um objeto timedelta:
    totalseconds - Retorna o deslocamento total de tempo somente em segundos
    days - Retorna o número de dias de diferença
    seconds - Retorna o número de segundos de diferença
    microseconds - Retorna o número de microsegundos de diferença
    min - O menor valor possivel para um objeto timedelta -999999999
    max - O maior valor possivel para um objeto timedelta (days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999).
    resolution - A menor dfirença possivel entre dois objetos timedelta 1 microsecondsw

Operações suportadas: 
    datetime = datetime + timedelta - Soma um deslocamento de tempo, a um objeto datetime
    datetime = datetime - timedelta - Subtrai um delocamento de tempo a um objeot datetime
    datetime só suportam opereção de deslocamento de tempo de soma e subtração
    
    
    timedelta = timedelta + timedelta - Soma dois deslocamentos de tempo
    timedelta =  timedelta - timedelta - Subtrai dois deslocamentos de tempo
    timedelta =  timedelta * int/float - Multiplica o deslocamento por um inteiro/flutuante, o valor é normalizado e arredondado, conforme as regras do timedelta

    int/float = timedelta / ou // timedelta - Retorna um valor inteiro/flutuante a partir da divisão de dois objetos timedelta

    timedelta = timedelta / ou // int/float - Divide o valor do timedelta, o timedelta é normalizado e arredondado

    timedelta = timedelta % timedelta - Cria um novo objeto timedelta a partir do resto da divisão de objetos timedelta

    
objetos timedelta suportam comparações relacionais(gt, ge, nq, eq e etc) com objetos timedelta

"""

from datetime import timedelta, datetime

year = datetime(2023, 1, 1)

delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)

print(f"{delta!r}")


d = timedelta(microseconds=-1) #Noramlização e Arredondamento de argumentos negativos, pode ser surpreendente


print(repr(d))

obj1 = timedelta(4)
obj2 = timedelta(6)

print('Operations in, not same types objects: [datetime [op] timedelta]:')
print(year + obj1)
print(year - obj2)

print('')
print('Operations in, same types objects: [timedelta [op] timedelta]')
print(obj1 + obj2)
print(obj2 - obj1)
print(obj1 * 5)
print(obj2 / obj1)
print(obj2 / 3)
print(obj2 // obj1)
print(obj2 // 4)
print(obj2 % obj1)

print(obj1 > obj2)