from PySide6.QtGui import QKeyEvent, QKeySequence
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtWidgets import QPushButton, QLineEdit, QGridLayout, QLabel
from variables import BIG_FONT, MINIMUM_WIDTH
from typing import TYPE_CHECKING
import utils

if TYPE_CHECKING:
    from Main_Window import Window


class Info(QLabel):
    def __init__(self, *args):
        super().__init__(*args)
        self.setStyleSheet('font-size: 16px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


class buttom(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fonte = self.font()
        self.fonte.setPixelSize(20)
        self.setFont(self.fonte)
        self.setMinimumSize(25, 25)
        
    def isDotOrNumber(self):
        return self.text() in '0123456789.'

    def isOperator(self):
        return self.text() in 'C◀^/*-+='
    

class Display(QLineEdit):
    press_equal = Signal()
    press_back = Signal()
    press_clear = Signal()
    press_operator = Signal(str)
    press_number = Signal(str)
    press_neg = Signal()

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(f'font-size: {BIG_FONT}px;')
        self.setMinimumHeight(BIG_FONT * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumWidth(MINIMUM_WIDTH)

    def keyPressEvent(self, keyevent: QKeyEvent) -> None:
        
        if keyevent.text().isnumeric() or keyevent.text() == '.' :
            self.press_number.emit(keyevent.text())
            return keyevent.ignore()
        
        operators = {34: '^', 0: '/', 47: '/', 42: '*', 45: '-', 43: '+'}  #^ /
        
        if keyevent.key() in operators.keys(): 
            if keyevent.text() == '-':
                self.press_neg.emit()

            self.press_operator.emit(operators.get(keyevent.key()))
            return keyevent.ignore()   
    
        pressed_key =  QKeySequence(keyevent.key()).toString()

        dic_signal = dict[str, Signal]
        special_keys:dic_signal = {'Backspace': self.press_back, 'Enter': self.press_equal, 'Return': self.press_equal, 'Del': self.press_back, 'Esc': self.press_clear, '=': self.press_equal}

        if special_keys.get(pressed_key):
            special_keys.get(pressed_key).emit()
            return keyevent.ignore()    
        
        #Quando o metódo da parent class não é retornado, digitar teclas é desativado   

    
class LayoutGrid(QGridLayout):
    def __init__(self, display:Display, info:Info, window: 'Window',  *args) -> None:
        super().__init__(*args)
        self.input_box:Display = display
        self.result_box:Info = info
        self.main_window: 'Window' = window
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0',  '', '.', '='],
        ]
        self.history = []
   
    def make_slot(self, func, *args, **kwargs):
            def slot(check):
                return func(*args, **kwargs)
            return slot
    
    def make_keyboard_slot(self, func, *args):
        def slot(keypressed):
            return func(keypressed, *args)
        return slot

    
    def result_box_hasoperator(self):
        return  any(char in self.result_box.text() for char in '/*-+')
    
    def show_critical_error(self, msgerror):
        msg_box = self.main_window.make_msg_box()
        msg_box.setText(msgerror)
        msg_box.setStandardButtons(msg_box.StandardButton.Ok)
        msg_box.setIcon(msg_box.Icon.Critical)
        buttom = msg_box.exec()
        print(f'Clicou no Ok' if buttom == msg_box.StandardButton.Ok else 'fechou a janela')

    @Slot()
    def show_calc_result(self):
            try:
                if self.result_box.text()[-2::] == '**':
                    table = self.result_box.text().maketrans(utils.operators, ' '*len(utils.operators))
                    number = self.result_box.text().translate(table).strip()
                    if int(number) > 2 and len(self.input_box.text()) >= 4:
                        raise OverflowError
                    
                op = self.result_box.text()[-1]
                #Verifica se antes de apertar o igual, a result box termina com um operador, e a inputbox tem um número valido
                if op in utils.operators and utils.isValidNumber(self.input_box.text()):
                    result = str(eval((self.result_box.text() + self.input_box.text())))
                    self.result_box.setText(result)
                    self.input_box.clear()

            except IndexError:
                pass
            except (ZeroDivisionError , OverflowError , ValueError) as Error:
                self.show_critical_error(Error.__class__.__name__ if Error.__class__.__name__ != 'OverflowError' else 'Capacidade do processador excedida')                 

                self.input_box.clear()
                self.result_box.setText('Error')     
                       
    @Slot()
    def del_a_char(self):
        self.input_box.setText(self.input_box.text()[:-1:])

    @Slot()
    def clear_display(self):
        if self.input_box.text():
            self.input_box.clear()
        elif self.result_box.text():
            self.result_box.clear()

    @Slot(buttom) #função em resposta a um signal. Slot que recebe argumento do tipo buttom
    def insert_buttontext_in_display(self, butt:buttom):
        if not isinstance(butt, str):
            buttom_pressed:str = butt.text()
        else:
            buttom_pressed:str = butt
    
        current_text_in_display:str = self.input_box.text() + buttom_pressed
        #Ao clicar em um botão, vai haver uma checagem se a operação é valida, se não for, ele não vai deixar digitar esse número invalido
        if not utils.isValidNumber(current_text_in_display):
            return
        
        # Não deixa o usuário fazer  0 a esquerda
        try:
            if buttom_pressed == '0' and self.input_box.text()[0] == '0' and not '.' in self.input_box.text():
                return   
        except IndexError:
            pass

        self.input_box.insert(buttom_pressed)

    @Slot(buttom)
    def operator(self, butt:buttom):
        
        if isinstance(butt, buttom):
            buttom_pressed = butt.text()
        else:
            buttom_pressed = butt

        if buttom_pressed == '^':
            buttom_pressed:str = '**'

        current_text_in_display = self.input_box.text() + buttom_pressed


        #Permitindo várias operações
        if not self.result_box_hasoperator() and utils.isValidNumber(self.result_box.text()) and not utils.isValidNumber(self.input_box.text()):
            return
        elif (utils.isValidNumber(self.result_box.text()) or self.result_box.text() == 'Error') and utils.isValidNumber(self.input_box.text()):
            self.result_box.setText(current_text_in_display)
            self.input_box.clear()
        
        #Checa se digitou um número antes de pressionar o operador
        if utils.isValidNumber(self.input_box.text()) :
            self.result_box.setText(self.result_box.text() + current_text_in_display)
            self.input_box.clear()
            return
        
    @Slot(buttom)
    def negative_number(self):    
        if not self.input_box.text() and '-' not in self.input_box.text():
            self.input_box.insert('-')
    
    @Slot()
    def display_in_focus(self):
        self.input_box.setFocus()


    def make_standard_gui(self):
        self.input_box.press_equal.connect(self.show_calc_result)
        self.input_box.press_back.connect(self.del_a_char)
        self.input_box.press_clear.connect(self.clear_display)     
        self.input_box.press_neg.connect(self.negative_number)
        self.input_box.press_number.connect(self.make_keyboard_slot(self.insert_buttontext_in_display))   
        self.input_box.press_operator.connect(self.make_keyboard_slot(self.operator))
        
        for row, iconlist in enumerate(self._grid_mask):
            for column, icon in enumerate(iconlist):
                butt = buttom(icon)

                butt.clicked.connect(self.make_slot(self.display_in_focus))

                if not butt.isDotOrNumber() and icon:
                    cmds = {
                        'C': self.clear_display,
                        '◀': self.del_a_char,
                        '=': self.show_calc_result
                    }
                    butt.setProperty('cssClass', 'specialButton') #Só os botões com essa propriedade e valor vão receber a  configuração de estilo
                    if cmds.get(icon):
                        butt.clicked.connect(self.make_slot(cmds.get(icon)))
                        
                    else:
                        if icon == '-':
                            butt.clicked.connect(self.make_slot(self.negative_number))
                        butt.clicked.connect(self.make_slot(self.operator, butt))
                elif icon:    
                
                    #Adicionando um slot(função em resposta a um signal) em todos os botões que não são operadores
                    my_slot = self.make_slot(
                    self.insert_buttontext_in_display,  butt
                    )

                    butt.clicked.connect(my_slot)

                
                if icon != '0' and icon:
                    self.addWidget(butt, row, column)
                elif icon:
                    self.addWidget(butt, row, column, 1, 2)

