from typing import Callable
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGroupBox, QHBoxLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from base.interfaces import InterfacesBase
from .form_v_layout import FormVLayout
from .line_edit_group import LineEditGroup
from .line_edit import LineEdit

class InterfacesGUI( InterfacesBase ):
    def __init__( self, name, parent=None ):
        super().__init__( parent )
        self._user_input : LineEditGroup
        self._user_output : LineEditGroup

    def get_name( self ):
        return self._modul_name

    def set_name( self, name ):
        self._modul_name = name

    def set_input( self, user_input : LineEditGroup ):
        self._user_input = user_input

    def set_output( self, user_output : LineEditGroup ):
        self._user_output = user_output

    def _add_getter( self, name, options : dict ):
        line_edit = LineEdit( name )

        if options["func"] == float:
            line_edit.setValidator( QDoubleValidator( line_edit ) )
        elif options["func"] == int:
            line_edit.setValidator( QIntValidator( line_edit ) )

        self._user_input.add_line_edit( line_edit )

    def add_func( self, name, func : Callable[ [dict], None ], **options ):
        # if not name in self._list_func:
            # self._list_func[name] = func

        line = LineEdit(name)
        line.setValidator( QDoubleValidator( line ) )

        line.setReadOnly( True )

        self._user_output.add_line_edit( line )
