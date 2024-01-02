"""
Cria uma classe para MainWindow, e cria uma isntância dessa classe e execute

Cada funcionalidade/comportamento da aplicação vai ficar em um metódo
e suas caracteristicas vão estar nos atributos de inicialização

"""
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication()
class Window_App(QMainWindow):...



if __name__ == '__main__':
    main_window = Window_App()
    main_window.show()
    app.exec()