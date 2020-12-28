from PyQt5.QtWidgets import QGroupBox, QVBoxLayout
from PyQt5.QtCore import Qt

class ModulWidget( QGroupBox ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self.layout = QVBoxLayout( self )
        self.layout.setAlignment( Qt.AlignTop )

        self._modul = None

    def set_modul( self, modul ):
        self._modul = modul

    def get_modul( self ):
        return self._modul
