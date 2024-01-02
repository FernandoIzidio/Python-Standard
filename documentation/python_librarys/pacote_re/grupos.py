"""

(abc) - Para uma ocorrencia ser valida, precisa ter abc, nessa ordem e juntos, ou seja precisa ter esse conjunto dentro da string para que ocorra uma ocorrência

() - \1
(()) - \1 \2
(() ()) - \1 \2 \3


em RE com grupos, só oque esta dentro do grupo que é retornado como ocorrência

search -  Primeira ocorrência e posição -> objeto regexp
findall - Retorna todas as ocorrência -> list
sub - Substitui uma ocorrência dentro de um texto por outra coisa -> str
compile - Cria um objeto regexp, que vai buscar sempre o mesmo padrão

grupos são salvos na memória, e podem ser acessados por \n, apenas na mesma expressão regular

?: - Remove grupo da memória
(?P<tag>) - Cria grupo nomeado
"""
import re
html = "<p>Frase</p> <p>Eita</p> <p>Trucoooooo</p> <div>Pegaaaa a LAPADAAAAA</div>" 
opensign = r'(<[pdiv]+>)'
closesign = r'(<\/+[pdiv]+>)'
print('Tags de abertura:', re.findall(opensign, html))
print('Tags de Fechamento:', re.findall(closesign, html))
print('Conteúdos: ', re.findall(r'<[pdiv]+>(.+?)<\/+[pdiv]+>', html))
print('\n\n\n\n')
for tupla in re.findall(r'(<([pdiv]{1,3})>(.*?)<\/\2>)', html):
    fullexp, tagname, content = tupla
    print(f"{fullexp=}")
    print(f'{tagname=}')
    print(f'{content=}')



print('\n\n\n\n')
print(re.findall(r'(?:<([pdiv]{1,3})>(.*?)<\/\1>)', html))


def check_cpf(cpf):
    cpf = re.findall(r'^((?:[0-9]{3}[-.]){3}[0-9]{2})$', cpf)
    if cpf:
        return 'Cpf válido'
    return 'Cpf Invalido'

cpf = "124.457.132-59"

print(check_cpf(cpf))
print('\n\n\n\n')
print(re.sub(r'(<([pdiv]{1,3})>)(.*?)(<\/\2>)', r' \1Um pouco mais de conteudo\3 \4', html))
print('\n\n\n\n')

print(check_cpf('a 123.456.789-09'))
print(check_cpf('123.456.789-09 fads'))

print(''.join([f'{caracter} ' for pos, caracter in enumerate(re.findall(r'([^.-]*)', cpf)) if caracter]).strip().split(' '))