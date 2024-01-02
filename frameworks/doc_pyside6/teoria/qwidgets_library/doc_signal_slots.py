"""
Slots - São funções que são executadas quando o signal de um widget é ativado, ou seja são funções
que são executadas toda vez que um widget sofre uma ação

Signal é qualquer tipo de ação que um widget sofre

Action - É uma opção de uma menuBar.

Slot é um função a ser executada em resposta a um signal/ação sofrida pelo widget

Todo signal pode enviar argumentos para um slot(função em resposta a signal), por exemplo QPushButtom em todos os seus signals sempre envia se o botão está marcado ou não para todos os slots então por isso que muitos slots(funções em resposta a signal) muitas vezes precisam ser adiados a execução, para que o slot funcione adequadamente

Resumindo é bem comum ter closures, para receber os argumentos do signal, e executar a função do slot

Para criar signal's usa-se PySide6.QtCore.Signal em atributos de classe

signal de actions:
    triggered - Verifica vez que a widget é clicada, ou executado por atalho
    toggled - Verifica toda vez que o estado de uma widget checkbox é alterado
    hovered - Verifica toda vez que um mouse passar por cima de um widget

signal de widgets:
    clicked - Verifica toda vez que o botão foi clicado
"""