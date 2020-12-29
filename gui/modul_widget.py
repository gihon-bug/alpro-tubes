from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QScrollArea, QWidget
from PyQt5.QtCore import Qt
from .perhitungan_widget import PerhitunganWidget

class ModulWidget(  QGroupBox ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self.layout = QVBoxLayout( self )

        self._button_layout = QHBoxLayout()
        self.layout.addLayout( self._button_layout )

        self._add_button = QPushButton( "Add", self )
        self._clear_value_button = QPushButton( "Clear Value", self )
        self._remove_button = QPushButton( "Remove", self )
        self._clear_modul_button = QPushButton( "Clear Table", self )

        self._button_layout.addWidget( self._add_button )
        self._button_layout.addWidget( self._clear_value_button )
        self._button_layout.addWidget( self._remove_button )
        self._button_layout.addWidget( self._clear_modul_button )

        self.layout.setAlignment( Qt.AlignTop )

        self.scroll_area = QScrollArea( self )
        self.scroll_area.setSizePolicy( QSizePolicy.Minimum, QSizePolicy.MinimumExpanding )
        self.scroll_layout = QVBoxLayout( self.scroll_area )
        self.scroll_layout.setAlignment( Qt.AlignTop )

        self.modul_group = QWidget( self )
        self.scroll_area.setWidget( self.modul_group )
        self.scroll_area.setWidgetResizable( True )

        self.layout.addWidget( self.scroll_area )

        self._add_button.clicked.connect( self.add_modul )
        self._remove_button.clicked.connect( self.pop_modul )
        self._clear_modul_button.clicked.connect( self.clear_modul )
        self._clear_value_button.clicked.connect( self.clear_value )

        self._modul = None

    def set_modul( self, modul ):
        self._modul = modul
        self.add_modul()

    def get_modul( self ):
        return self._modul

    def add_modul( self ):
        if self._modul is not None:
            widget = PerhitunganWidget( self )
            widget.set_modul( self._modul )
            widget.setSizePolicy( QSizePolicy.Minimum, QSizePolicy.Minimum )
            self.modul_layout.addWidget( widget )
            widget.adjustSize()

    def pop_modul( self ):
        pass

    def clear_modul( self ):
        pass

    def clear_value( self ):
        pass