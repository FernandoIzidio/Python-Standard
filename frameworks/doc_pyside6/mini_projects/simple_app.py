"""

"""
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QGridLayout, QPushButton)

app = QApplication()
main_window = QMainWindow()
Main_WidGet = QWidget()
Layout = QGridLayout()
status_bar = main_window.statusBar()
menu_bar = main_window.menuBar()


main_window.setCentralWidget(Main_WidGet) #Define a main Widget
Main_WidGet.setLayout(Layout) #Define o layout da Main Widget

#Definindo os Widgets da aplicação
def Implement_Style(*widgets, **styles:dict):
    for box in widgets:
        set_style = getattr(box, 'setStyleSheet')
        QCss = ''
        for chave, valor in styles.items():
            QCss += f'{chave}: {valor};'
        set_style(QCss)

def Append_Box(row: int, *widgets: QPushButton):
    for pos, box in enumerate(widgets, start=1):
        Layout.addWidget(box, row, pos)



Mainbuttom = QPushButton('My System Calc')
Mainbuttom.setStyleSheet('width: 200px; background-color: #FF0554; color: #FFFFFF;')

Layout.addWidget(Mainbuttom, 1, 1, 1, 3)
for count in range(1, 8, 3):
    box1, box2, box3 = QPushButton(str(count)), QPushButton(str(count + 1)), QPushButton(str(count + 2))
    Implement_Style(box1, box2, box3, **{'background-color': "#000000", 'color': '#FFFFFF'})

    if count < 4:
        Append_Box(2, box1, box2, box3)
    elif count < 7:
        Append_Box(3, box1, box2, box3)
    else:
        Append_Box(4, box1, box2, box3)

opt = menu_bar.addMenu('Options')
opt_option = opt.addAction('First')

app.exec()
