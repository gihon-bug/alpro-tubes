from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import Qt
from base.modul import Modul

class PerhitunganWidget( QWidget ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self._modul : Modul
        self._modul = None

        self.layout = QGridLayout( self )
        self.layout.setAlignment( Qt.AlignTop )

    def set_modul( self, modul ):
        self._modul = modul