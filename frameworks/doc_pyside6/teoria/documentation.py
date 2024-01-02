"""
Biblioteca excelente para criação de interfaces graficas

É uma biblioteca multi-plataforma que funciona windows, linux, MAC, e é baseado em C++

PyQT - é uma biblioteca com licensa GPL(General Public License), oque obriga o software a ser open-source

MIT-  não tem copyright

PySide6 - é uma biblioteca com licensa LGPL(Lesser General Public License), que permite que o software seja comercializado

-> QApplication - Gerencia a aplicação, inicia, gerencia recursos, e outros nuances relacionadas ao gerenciamento da aplicação
    -> QMainWindow - Define/Implementa a central Widget
        -> Central Widget(Caixa Interativa Central) - Define que toda a aplicação vai ser construida em cima de uma caixa interativa
            -> Layout - Define o layout do Central_Widget
              ->  widgets(caixas interativas)


QTWidgets - É uma biblioteca que fornece suporte para multiplos elementos de interação em uma GUI

Widgets - Elemento de interação dentro de uma interface grafica

QAAplication O QApplication é responsável por iniciar a aplicação GUI, configurar o ambiente,
gerenciar eventos de aplicativo e coordenar recursos de GUI


"""
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout


app = QApplication()

buttom = QPushButton('Finish')
buttom.setStyleSheet('font-size: 40px; padding: 8px; background-color: #FF12FF; color: #FFFFFF;')
buttom2 = QPushButton('Finish2')
widget_manager = QWidget()
layout = QVBoxLayout()
widget_manager.setLayout(layout)
layout.addWidget(buttom)
layout.addWidget(buttom2)
widget_manager.show()#Mostra caixa pai interativa
app.exec()