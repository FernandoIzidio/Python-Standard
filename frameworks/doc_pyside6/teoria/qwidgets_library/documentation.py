"""
Biblioteca QtWidgets fornece muitos widgets(caixas interativas) para construção de uma aplicação

-> QApplication - Gerencia a aplicação, inicia, gerencia recursos, e outros nuances relacionadas ao gerenciamento da aplicação
    -> QMainWindow - Define/Implementa a central Widget
        -> Central Widget(Caixa Interativa Central) - Define que toda a aplicação vai ser construida em cima de uma caixa interativa
            -> Layout - Define o layout da Central_Widget
              ->  widgets(caixas interativas)



QtWidgets - É uma biblioteca que fornece suporte para multiplos elementos de interação em uma GUI

Widgets - Elemento de interação dentro de uma interface grafica

QAAplication O QApplication é responsável por iniciar a aplicação GUI, configurar o ambiente,
gerenciar eventos de aplicativo e coordenar recursos de GUI


Classes da biblioteca QtWidgets:
    QApplication - Reponsavel por iniciar a aplicação e e gerenciar seus recursos
    QMainWindow -  Reponsavel por garantir que toda aplicação seja feita em um unica janela, e por ter widgets já predefinidos(statusBar, menuBar), também define o centralWidget
    Qlabel - Pode ser usado para exibir textos ou imagens dentro de uma aplicação
    QPushButtom - Usado para criar um botão
    QWidget - Usado para criar widgets comuns ou central widgets
    Qboxlayour - Responsavel por definir o layout dos widgets filhos do central widget
    QLineEdit - Widget usado para entrado de dados curtos(em uma linha)
    QTextEdit - Widget usado para entrada de dados longas


"""
from PySide6.QtWidgets import QMainWindow, QWidget