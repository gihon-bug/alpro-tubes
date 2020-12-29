from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtCore import Qt
from .form_v_layout import FormVLayout
from .line_edit import LineEdit

class LineEditGroup( QGroupBox ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self.layout = FormVLayout( self )
        self.layout.setAlignment( Qt.AlignTop)

        self._line_edit = {}

        self._row = 0
        self._col = 0

        self._row_limit = -1
        self._column_limit = -1

    def set_cell_limit( self, row, col ):
        self.set_column_limit( col )
        self.set_row_limit( row )

    def set_column_limit( self, col ):
        self._column_limit = col

    def set_row_limit( self, row ):
        self._row_limit = row

    def add_line_edit( self, item : LineEdit ):
        self._line_edit[ item.get_name() ] = item
        self.layout.addWidget( item.get_name(), self._line_edit[ item.get_name() ], self._row, self._col )

        self._col += 1

        if self._col >= self._column_limit:
            self._row += 1
            self._col = 0
