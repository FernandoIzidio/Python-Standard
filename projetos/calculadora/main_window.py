from visual_widgets import Display, Info
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox


class Window(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.central_widget = QWidget()
        self.cw_layout = QVBoxLayout()
        #Input box
        self.input_box = Display()

        #Info/result box
        self.result_box = Info('')

        self.central_widget.setLayout(self.cw_layout) 
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Calculadora')

    #Adiciona ao main layout
    def add_widget_2mainlayout(self, widget: QWidget):
        self.cw_layout.addWidget(widget)
    
    #Aplicação com janela de tamanho fixo
    def window_fixed_size(self) -> None:
        self.adjustSize() #Garante que todoso widgets caimbam no layout
        self.setFixedSize(self.width(), self.height()) #Define que a janela vai ter um tamanho fixo, igual ao tamanho atual da MainWindow
        
    def make_msg_box(self):
        return QMessageBox(parent=self) #Parent da message box vai ser um instância da main window, ou seja o parent da message box vai ser a janela atual, e a message box não precisa ser adicionado ao layout, só precisa ser associada a uma window

