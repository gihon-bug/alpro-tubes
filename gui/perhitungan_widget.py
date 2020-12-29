from PyQt5.QtWidgets import QGroupBox, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from base.modul import Modul
from .interfaces import InterfacesGUI
from .line_edit_group import LineEditGroup, LineEdit

class PerhitunganWidget( QGroupBox ):

    def __init__( self, parent=None, modul : Modul = None ):
        super().__init__( parent )
        self._modul : Modul
        self._modul = None
        self.set_modul( modul )

        self.layout = QHBoxLayout( self )
        self.setLayout( self.layout )

        self._interfaces = InterfacesGUI("")

        self._user_input = LineEditGroup( self )
        self._user_input.set_column_limit( 3 )
        self._user_output = LineEditGroup( self )
        self._user_output.set_column_limit( 1 )

        self._interfaces.set_input( self._user_input )
        self._interfaces.set_output( self._user_output )

        self.layout.addWidget( self._user_input, 3 )
        self.layout.addWidget( self._user_output, 1 )

    def set_modul( self, modul ):
        if self._modul is not modul:
            self._modul = modul
            self._interfaces.set_name( modul.name )

            modul_inst = modul()
            modul_inst.get_value( self._interfaces )


    def clear_modul( self ):
        i = 0
        length = len( self._interfaces )
        while i < length:
            self.pop_modul()
            i += 1

    def clear_value( self ):
        pass