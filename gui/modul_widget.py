from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QScrollArea, QWidget
from PyQt5.QtCore import Qt
from .perhitungan_widget import PerhitunganWidget
from .modul_group import ModulGroup

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

        self._add_button.clicked.connect( self.add_modul )
        self._remove_button.clicked.connect( self.pop_modul )
        self._clear_modul_button.clicked.connect( self.clear_modul )
        self._clear_value_button.clicked.connect( self.clear_value )

        self._modul_group = ModulGroup( self )

        self.layout.addWidget( self._modul_group )

        self._modul = None

    def set_modul( self, modul ):
        self._modul = modul
        self._modul_group.set_modul( modul )
        self.add_modul()

    def get_modul( self ):
        return self._modul

    def add_modul( self ):
        self._modul_group.add_modul()

    def pop_modul( self ):
        pass

    def clear_modul( self ):
        pass

    def clear_value( self ):
        pass