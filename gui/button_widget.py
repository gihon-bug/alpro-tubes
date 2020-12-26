from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from base.modul import Modul

class ButtonWidget( QGroupBox ):
    clicked = pyqtSignal()
    def __init__( self, content : set ):
        super().__init__( content )

        self.layout = QVBoxLayout()
        self.setLayout( self.layout )

        self._modul = {}

    def set_modul( self, list_modul ):
        self._modul = list_modul

        self.button = []
        for name, value in list_modul.items():
            print(name)
            button = QPushButton( name, self )
            self.layout.addWidget( button )
            self.button.append( button )

    def onButtonClicked( self ):
        pass
