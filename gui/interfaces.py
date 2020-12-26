from typing import Callable
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from base.interfaces import InterfacesBase
from .line import LineEdit

row_limit = 3
getter_row_limit = 2
result_rpw_limit = row_limit - getter_row_limit

class InterfacesGUI( InterfacesBase ):
    def __init__( self, name ):
        self.set_name( name )
        self._list_func = {}
        self._layout = QGridLayout()
        self._layout.setAlignment( Qt.AlignTop )
        self._widgets = QWidget()
        self._widgets.setLayout( self._layout )
        self._layout_getter_pos = {
            "column" : 0,
            "row" : 0 ,
            "limit_column" : 2,
            "limit_row" : -1,
            "start_column" : 0,
            "start_row" : -1
        }

        self._layout_result_pos = {
            "column" : 0,
            "row" : 0,
            "limit_column" : 2,
            "limit_row" : -1,
            "start_column" : 2,
            "start_row" : -1
        }

    def set_parent( self, parent=None ):
        if parent is not None:
            parent.addWidget( self._widgets )
        self._widgets.show()

    def get_widgets( self ):
        return self._widgets

    def get_name( self ):
        return self._modul_name

    def set_name( self, name ):
        self._modul_name = name

    def _add_widgets( self, name, item : QWidget, cell : dict ):
        if cell["column"] < cell["start_column"]:
            cell["column"] = cell["start_column"]

        if cell["column"] == cell["limit_column"] + cell["start_column"]:
            cell["column"] = cell["start_column"]
            cell["row"] += 2

        row = cell["row"]
        column = cell["column"]

        label = QLabel( name )
        self._layout.addWidget(
            label,
            row,
            column
        )

        self._layout.addWidget(
            item,
            row + 1,
            column
        )


    def _add_getter( self, name, options : dict ):
        text = LineEdit( name )
        
        if options["func"] == float:
            text.setValidator( QDoubleValidator( text ) )
        elif options["func"] == int:
            text.setValidator( QIntValidator(text) )
            
        text.adjustSize()

        self._add_widgets(
            name,
            text,
            self._layout_getter_pos
        )
        
        self._layout_getter_pos["column"] += 1


        self._widgets.adjustSize()
    
    def add_func( self, name, func : Callable[ [dict], None ], **options ):

        if not name in self._list_func:
            self._list_func[name] = []

        line = LineEdit(name)
        line.setValidator( QDoubleValidator( line ) )

        line.setReadOnly( True )
        self._add_widgets(
            name,
            line,
            self._layout_result_pos
        )
            
        self._list_func[name].append( func )

