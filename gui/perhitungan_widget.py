from PyQt5.QtWidgets import QScrollArea, QGroupBox, QVBoxLayout
from PyQt5.QtCore import Qt
from base.modul import Modul
from .interfaces import InterfacesGUI

class PerhitunganWidget( QScrollArea ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self._modul : Modul
        self._modul = None

        self.group_modul = QGroupBox( self )
        self.group_layout = QVBoxLayout( self.group_modul )
        self.group_layout.setAlignment( Qt.AlignTop )

        self.setWidget( self.group_modul )
        self.setWidgetResizable( True )

        self._interfaces = []

    def set_modul( self, modul ):
        if self._modul is not modul:
            self.clear_modul()
            self._modul = modul
            self.add_modul()

    def clear_modul( self ):
        for i in range( len( self._interfaces ) ):
            self.pop_modul()

    def pop_modul( self ):
        interface = self._interfaces.pop( len(self._interfaces) - 1 )
        self.group_layout.removeWidget( interface.get_widgets() )
        interface.delete_widgets()

    def clear_value( self ):
        pass

    def add_modul( self ):
        if self._modul is not None:
            interface = InterfacesGUI( self._modul )
            self.group_layout.addWidget( interface.get_widgets() )

            modul = self._modul()
            modul.get_value( interface )

            self._interfaces.append( interface )
