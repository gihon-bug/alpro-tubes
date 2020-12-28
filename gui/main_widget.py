from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy, QPushButton
from PyQt5.QtCore import Qt
from .button_widget import ButtonWidget
from .modul_widget import ModulWidget

class MainWidget( QWidget ):
    def __init__( self, parent=None ):
        super().__init__( parent )

        self.layout = QHBoxLayout( self )
        self.setLayout( self.layout )
        self.layout.setAlignment( Qt.AlignTop )

        self._modul = {}

        self._button_widget = ButtonWidget( self )
        self._button_widget.setSizePolicy( QSizePolicy.MinimumExpanding, QSizePolicy.Expanding )


        self._modul_layout = QVBoxLayout()
        self._modul_layout.setAlignment( Qt.AlignTop )

        self._add_modul_button = QPushButton("Add")
        self._add_modul_button.clicked.connect( self.add_modul )
        self._modul_layout.addWidget( self._add_modul_button )

        self._modul_widget = ModulWidget( self )
        self._modul_widget.setSizePolicy( QSizePolicy.MinimumExpanding, QSizePolicy.Expanding )

        self._modul_layout.addWidget( self._modul_widget, 10 )

        self.layout.addWidget( self._button_widget, 1  )
        self.layout.addLayout( self._modul_layout, 5 )
        self._button_widget.adjustSize()

    def set_modul( self, list_modul : dict ):
        self._modul = list_modul

    def start( self ):
        self._button_widget.set_modul( self._modul )
        self._button_widget.adjustSize()
        self._button_widget.clicked.connect( self.change_modul )

    def add_modul( self ):
        pass

    def change_modul( self, modul ):
        pass
