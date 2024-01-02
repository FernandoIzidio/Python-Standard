"""
Função recursiva é um loop que pode ser usado em qualquer trecho do código.
Toda função recursiva tem um limite de recursão, então para evitar quebra de aplicações, sempre trate esse erro de Recursion Limites.

Loops de validação de entrada, Loops de login e etc

Funções recursivas devem ser usadas para problemas simples, com divisões de problemas claros, mas no python essas funções são mais lentas que loops iterativos, pois a cada recursão, é adicionado uma pilha na callstack, e em linguagens que não otimizam recursão como python, ela pode gerar stack over flow, gerar bugs, deixar o código mais lento e propenso a ataques DDOS

Funções recursivas são recomendas para acessar extrutura de dados, ou arquivos que são problemas previsiveis

funções com loop embutido tem desempenho melhor que as recursivas


-Função que funciona como loop 
-Função que chama a si mesma
-Serve para diminuir problemas grandes, em problemas menores
-Ela salva valores até o fim da recursão
"""
#Em algum momento a fatorial(n) vai valer 1
def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)
    
print(fatorial(5))
print(fatorial(4))
print(fatorial(3))

