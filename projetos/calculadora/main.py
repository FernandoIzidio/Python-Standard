"""
"""
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from visual_widgets import LayoutGrid
from Main_Window import Window
from variables import ROOT_FOLDER, IMAGES_FOLDER
import styles, sys



if __name__ ==  "__main__":
    app = QApplication(sys.argv)
    styles.setup() #Setup the darktheme in app

    main_window = Window() 


    icone  = QIcon(str(IMAGES_FOLDER / 'icon.png'))

    #Setting the icon
    main_window.setWindowIcon(icone)
    app.setWindowIcon(icone)
    
    
    #Adicionei widgets não grid
    main_window.add_widget_2mainlayout(main_window.result_box)
    main_window.add_widget_2mainlayout(main_window.input_box)

    #Criei o grid layout depois de adicionar os non-grid, para ao grid começar a adicionar depois da linha daqueles primeiros non-grids
    GridLayout = LayoutGrid(main_window.input_box, main_window.result_box, main_window)
    main_window.cw_layout.addLayout(GridLayout)
    GridLayout.make_standard_gui()
    
    

    main_window.window_fixed_size()
    main_window.show()
    app.exec()