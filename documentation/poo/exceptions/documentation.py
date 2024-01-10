"""-*- coding: utf-8 -*-
Exceptions personalizadas:
    --Exceptions personalizadas é um conceito muito util para comunicar um erro em um software quando os erros padrões, não conseguem suprir a necessidade de explicar de maneira clara o código.

    -Para criar uma exception basta herdar da classe exceptions

    
    -em versões mais recentes do python é possivel adicionar notas a objetos da classe erro.
    erro.add_note()

    __notes__ - Retorna notas de erro
    __traceback__ - Retorna traceback do erro
    __args__ - Retorna argumentos passados para o erro
    
    alguns outros metódos e atributos uteis:
        -args - todas mensagens passados pro __init__ do objeto do erro.
        -add_note(args) - Adiciona argumentos, itens a lista __notes__
        -with_traceback(tb) - Modifica o traceback de um erro
    args - devem ser a explicação principal do erro
    notes - explicações adicionais do erro
"""

try:
    raise TypeError('Deu um erro')
except Exception as error:
    error.add_note('mais alguns erros')
    print(error.args) #Printa argumentos de erro
    print(error.__notes__) #Printa notas de erro
    othererror = ValueError('OCORREU OUTRO ERRO')
    othererror.with_traceback(error.__traceback__)
    raise othererror from error
