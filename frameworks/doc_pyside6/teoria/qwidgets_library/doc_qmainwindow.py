"""
MainWindow - Defina a janela principal que vai conter a aplicação, e implementa a Caixa interativa principal(Central_Widget)

MainWindow tem muitas caixas interativas/widgets já pré implementadas(menuBar, statusBar)

Action é uma opção dentro de um menu

Cada widget, action, menu e etc, carrega um signal em especifico(triggered, hovered, toggled, clicked e etc)

A mainwindow deve acomador a central_widgets e o s child widgets

Metódos uteis de MainWindow:
    setCentralWidget(QWidGet) - Define qual vai ser a caixa interativa principal(CentralWidget)
    setWindowIcon(QtGUI.QIcon) - Define um icone para a mainwindow
    statusBar() - Retorna o widget correspondente a Status Bar
    setWindowTitle(title:str) - Define o título da janela
    menuBar() - Retorna o widget correspondente ao MenuBar
    adjustSize() - Garante que todos widgets da aplicação sejam visiveis na main windows
    setHeightfixed() - Define uma altura fixa
    setWidthfixed() - Define uma largura fixa
    
    width() -  retorna a largura atual da MainWindow.
    self.height() = retorna a altura atual do MainWindow.

Metódos de StatusBar widget:
    showMessage(msg:str) - Mostra uma mensagem na barra de status


Metódos Uteis de MenuBar:
    add_menu(name:str)-> boxmenu - Cria um menu na menubar

Metódos Uteis de BoxMenu:
    add_action(name:str) -> BoxAction - Cria uma opção dentro de um menu

Metódos Uteis de BoxAction:
    triggered(provocado) - Verifica se a opção/ação foi clicada, executada por atalho
        triggered.connect(func) - Se a opção/ação foi clicada, ou executada por atalho
            ele vai executar uma metódo/função(slot)

    toggled(alterado) - Verifica toda vez que o estado de uma widget/action checkbox é alterado.
        toggled.connect - Se o estado da action/widget for alterado, ele vai executar uma função/metódo/slot
        obs: Toggled toda vez que o estado da action é alterado, quando ele chama um slot, ele vai por padrão
        passar o seu estado para o slot

    hovered - Verifica toda vez que o mouse é passado por cima de action







"""
