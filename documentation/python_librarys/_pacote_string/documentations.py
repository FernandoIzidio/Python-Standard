"""
Pacote String:
    -Possui muitas funções uteis para trabalhar com objetos unicode, e para manipular strings
    -Util para saber quais tipos de caracters são suportados no python, ou para passar valores para variaveis em documentos de texto
    - ascii_letters - Retorna letras do python que estão na codificação ascii
    - digits - Números decimais do python
    - punctation - Retorna a pontuação suportada pelo python

    template(conteudo:str) - Cria um texto string com delimitador de vars sendo $
        -substitute(iterable) -> str - substitui variaveis por valores informados no iterable, ou argumento nomeados

$ - Delimitador padrão de variaveis em templates
{} - Usado para separar variavel de texto, quando estão colados
        """

import string
from pathlib import Path

Waydir = Path(__file__).parent / 'Documento.txt'
Waydir.touch()

msg ="""Prezado(a) ${nome},

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso deseje cancelar o serviço, entre em contato com a ${empresa} pelo telefone ${telefone}.

Atenciosamente,

${empresa}, 
"""

              
dados = dict(
    nome='Joao',
    valor= 5000,
    data= '10/05/2009',
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

conteudo = string.Template(msg)

Waydir.write_text(conteudo.substitute(dados))