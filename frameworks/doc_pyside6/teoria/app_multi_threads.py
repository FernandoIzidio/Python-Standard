"""

"""
from typing import cast
from typing import Optional
from PySide6.QtCore import QThread, QObject, Signal, Slot, QEvent
from thread_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from PySide6.QtGui import QKeyEvent, QKeySequence
from time import sleep
import sys

class Other_Thread(QObject):
    started = Signal()
    progress = Signal(str)
    finished = Signal()

    def __init__(self, *args) -> None:
        super().__init__(*args)

    
    def run(self):
        self.started.emit()
        for count in range(10):
            sleep(1)
            self.progress.emit(F'{count}')

        self.finished.emit()



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args)-> None:
        super().__init__(*args)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.makeslot(self.save_file))
        self.pushButton_2.clicked.connect(self.makeslot(self.check_status))
        self.lineEdit.installEventFilter(self)

    @Slot()
    def makeslot(self, func, *args):
        def slot(checked):
            func(*args)
        return slot
    
    def threadslot(self, func, *args):
        def slot(num):
            func(num, *args)
        return slot
    
    def eventFilter(self, watched, event,  *args) -> bool:
        if watched == self.lineEdit and event.type() == QEvent.KeyPress:
            event: QKeyEvent 

            if QKeySequence(event.key()).toString() == 'Backspace':
                self.label.setText(self.label.text()[:-1:])
            else:
                self.label.setText(self.label.text() + event.text())
            

        
        return super().eventFilter(watched, event, *args)
    


    def save_file(self):
        self.task = Other_Thread()
        self.thread_ = QThread()
        self.task.moveToThread(self.thread_)


        self.thread_.started.connect(self.task.run)
        self.task.finished.connect(self.thread_.quit)

        self.thread_.finished.connect(self.thread_.deleteLater)

        self.task.started.connect( self.lock_port)
        self.task.progress.connect( self.threadslot(self.show_progress))
        self.task.finished.connect( self.release_port)
        self.thread_.start()

    def release_port(self):
        self.pushButton.setDisabled(False)
        self.label.setText('Tarefa/Thread encerrada')

    def show_progress(self, arg_slot):
        self.label.setText(arg_slot)

    def lock_port(self):
        self.label.setText('Começou tarefa')
        self.pushButton.setDisabled(True)

    def check_status(self):
        self.label_2.setText('Ok')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    m_window = MainWindow()
    
    m_window.show()
    app.exec()