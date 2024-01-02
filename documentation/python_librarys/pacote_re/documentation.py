"""
Pacote Regular Expressions, usado para lidar com expressões regulares

Forma simples de identificar uma cadeia de caracteres que correspondam a um padrão
Identificar padrões

findall - Retorna todas as cadeias de caracters que correspondam ao padrão - lista
search(re, string) -> objeto regexp - Retorna primeira ocorrência do padrão, e a posição onde ocorreu
sub - Substitui partes de string que correspondam ao padrão - str
compile - É util para quando se precisa fazer diferentes tipos de buscas, sempre usando o mesmo padrão, cria uma re, sempre com o mesmo padrão de busca

metachars :
    . - Qualquer caracter exceto quebra de linha
    | - ou
    [] - Grupo de caracters, escolhe apenas um
    () - Cadeia de caracters, tem que corresponder ao grupo

Quantificadores:
    * - pode se repetir 0 ou mais vezes
    +  - 1 ou mais vezes
    ? - 0 ou 1 vez
    {,n} - 0 até n vezes
    {n,} - n ou mais vezes
    {n} - n vezes
    {n, n2} - De n até n2 vezes
    
     
Parametros:
    count - Define o número das primeiras ocorrências que serão substituidas


"""
import re


texto = "Este é um teste de expressões regulares, teste, teste"

re_object = re.search(r'teste', texto)
all_ocorrency = re.findall(r'teste', texto)
mod = re.sub(r'teste', 'Truco', texto, count=2) #Substitui as duas primeiras ocorrências
print(re_object)
print(all_ocorrency)
print(mod)


regexp = re.compile('teste')
print(regexp.search(texto))
print(regexp.findall(texto))
print(regexp.sub('Trucão', texto, 1))