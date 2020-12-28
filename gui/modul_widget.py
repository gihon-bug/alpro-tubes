from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
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

        self._perhitungan_widget = PerhitunganWidget( self )
        self._perhitungan_widget.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding )
        self.layout.addWidget( self._perhitungan_widget )

        self._add_button.clicked.connect( self._perhitungan_widget.add_modul )
        self._remove_button.clicked.connect( self._perhitungan_widget.pop_modul )
        self._clear_modul_button.clicked.connect( self._perhitungan_widget.clear_modul )
        self._clear_value_button.clicked.connect( self._perhitungan_widget.clear_value )

        self._modul = None

    def set_modul( self, modul ):
        self._modul = modul
        self._perhitungan_widget.set_modul( modul )

    def get_modul( self ):
        return self._modul

    def add_modul( self ):
        pass

    def remove_modul( self ):
        pass

    def clear_modul( self ):
        pass

    def clear_value( self ):
        pass