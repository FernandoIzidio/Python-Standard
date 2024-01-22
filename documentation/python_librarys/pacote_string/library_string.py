"""
Biblioteca string:
    Capwords(str, [sep]) -> self.str coverte cada palavra separada por espaço em uma string, em uma palavra que começa com maiusculo, assim cada palavra separada por espaço começa com letra maiuscula.
    Separador é opcional, para caso o separador das palavras não for um espaço em branco

    whitespaces - variavel que contém uma string predefinida que inclui todos os caracteres de espaço em branco, como espaços, tabulações e quebras de linha.
    \t - Tabulação
    \n - Quebra de linha
    \r - retorno
    \x0b - tabulação vertical
    \x0c'- quebra de página
    é util para quando se quer remover todo tipo de caractere de espaço e quebra de linha de  um iterable

    ascii_letter - Retorna todas as letras maisculas e minusculas suportadas pelo python
    ascii_lowercase - Retorna apenas as letras minúsculas
    ascii_uppercase - Retorna apenas a letras maiusculas suportadas pelo python
    punctuation - Retorna as pontuações suportadas pelo python
    digits - Retorna números decimais suportados pelo python
    hexdigits - Retorna número hexadecimais
    octdigits - Retorna números octais
    printable - Retorna todos os caracteres que são printaveis em python
    obj.formatter("texto {var}") - Cria um objeto que funciona basicamente como uma f-string


    formatter(str) = Template(str) - formatter e template fazem funções parecidas oque muda é o delimitador de variaveis

    obj = Template(conteudo:str) -> None
        a classe Template recebe um argumento conteudo do tipo str, esse argumento str conteudo que o template recebe de argumento, possui variaveis com delimitadores que podem ser substituidos posteriormente.
        Delimitador de var padrão: $var
        Classe muito util para manipular arquivos de texto de forma eficiente

        objtemplate methods:
            delimiter = $ -> Delimitador padrão de variaveis, de objetos template
            idpattern [r'\w[_a-z0-9]*']- é uma expressão regular que define como as variáveis são reconhecidas em um obj template
            pattern[r'\$(?:[^{](?:[^{}]+|{[^{}]*})*)}'] - Define quais caracteres podem separar o nome de uma variavel a ser delimitada por $ exemplo:
            ${var}textotexto 

            substitute(dict|kwargs) -> retorna string nova - Troca as variaveis delimitadas por $ pelos valores especificados no dict ou nas kwargs
                nota: Se uma variavel não receber seu valor ele retorna um erro falando que está faltando keyword arguments
            substitute_sage(dict|kwargs) -> retorna string nova - Faz a mesma coisa que o substitute mas suprime erros, caso falte chaves/valor, ou kwags a serem inseridos no template


"""

import string


texto = 'flamengo piada'
print(string.capwords(texto), type(string.capwords(texto)))

texto2 = 'The|quick|brown|fox|jumped|over|the|lazy|dog'
print(string.whitespace)
print(' '.join(string.capwords(texto2, sep='|').split('|')))

print(string.whitespace)

temp = string.Template('Olá $nome, seu saldo é $saldo')
msgsubstituida = temp.substitute({'nome': 'tulio', 'saldo': 500})
print(msgsubstituida.replace('500', 'R$ 500,00'))


TEMP2 = string.Template('Saldo em conta R$$ ${saldo}.')
conteudo = TEMP2.substitute(saldo=500)
print(conteudo)

print(string.whitespace)
values = {'var': 'foo'}
temp3 = string.Template("""
Variable : $var
Escape : $$
Variable in text: ${var}iable
""")
print('TEMPLATE:', temp3.substitute(values))







newtemp = """
Variable : %(var)s
Escape : %%
Variable in text: %(var)siable
"""
print('INTERPOLATION(Arcaico):', newtemp % values)

print(string.whitespace)

values = {'var': 'foo'}
temp = string.Template('texto /var /var')
temp.delimiter = '/'

print(temp)
print(string.whitespace)

class My_Template(string.Template):
    delimiter = '%'

print(string.Template("").pattern)