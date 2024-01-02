from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
import faker
fk = faker.Faker('')

app = QApplication()

main_window = QMainWindow()
main_window.setWindowTitle('My First Application')

central_widget = QWidget()
main_window.setCentralWidget(central_widget)

GLayout = QGridLayout()
central_widget.setLayout(GLayout)

status_bar = main_window.statusBar()

menubar = main_window.menuBar()
for count in range(4):
    menu = menubar.addMenu(fk.word())
    temp = fk.word().capitalize()
    opt = menu.addAction(temp)
    opt.triggered.connect(lambda status: status_bar.showMessage(f'{temp} foi clicado'))

othermenu = menubar.addMenu('Other Menu')
interrupt = othermenu.addAction('Interruptor')
interrupt.setCheckable(True)
interrupt.toggled.connect(lambda status: status_bar.showMessage('Interruptor está ligado') if interrupt.isChecked()
else status_bar.showMessage('Interruptor não está ligado'))

othermenu.hovered.connect(lambda status: othermenu.setStyleSheet('background-color: #F4A312;'))

buttom = QPushButton('Verifica')
GLayout.addWidget(buttom, 1, 1)
buttom.clicked.connect(lambda status: status_bar.showMessage('Interruptor está ligado') if interrupt.isChecked()
else status_bar.showMessage('Interruptor não está ligado'))

main_window.show()
app.exec()