from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
# from PyQt5.QtCore import 
from base.controller import ControllerBase

class ControllerGUI( ControllerBase ):
    def __init__( self ):
        super().__init__()
        self._app = QApplication([])

        self._window = QMainWindow()
        self._window.setWindowTitle("Rumus fisdas")
        self._window.setGeometry(300,300,400,400)

        self._label = []
    
    def start(self, modul : dict ):
        x = 20
        y = 20
        for name in modul.keys():
            label = QLabel( self._window )
            label.setText( name )
            label.move( x, y )
            y += 30
            self._label.append( label )
        self._window.show()
        return self._app.exec_()
