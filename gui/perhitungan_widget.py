from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from base.modul import Modul
from .interfaces import InterfacesGUI

class PerhitunganWidget( QGroupBox ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self._modul : Modul
        self._modul = None

        self.layout = QVBoxLayout( self )
        self.layout.setAlignment( Qt.AlignTop )

        self._interfaces = []

    def set_modul( self, modul ):
        if self._modul is not modul:
            self.clear_modul()
            self._modul = modul
            self.add_modul()

    def clear_modul( self ):
        for item in self._interfaces:
            item.delete_widgets()
        self._interfaces.clear()

    def remove_modul( self ):
        interface = self._interfaces.pop( len(self._interfaces) - 1 )
        interface.delete_widgets()

    def clear_value( self ):
        pass

    def add_modul( self ):
        if self._modul is not None:
            interface = InterfacesGUI( self._modul )
            self.layout.addWidget( interface.get_widgets() )

            modul = self._modul()
            modul.get_value( interface )

            self._interfaces.append( interface )
