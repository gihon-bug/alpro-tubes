from PyQt5.QtWidgets import QWidget
from base.modul import Modul

class PerhitunganWidget( QWidget ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self._modul : Modul

    def set_modul( self, modul ):
        self._modul = modul