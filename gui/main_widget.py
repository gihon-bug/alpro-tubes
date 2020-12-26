from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from .button_widget import ButtonWidget
from .perhitungan_widget import PerhitunganWidget

class MainWidget( QWidget ):
    def __init__( self, parent=None ):
        super().__init__( parent )

        self.layout = QHBoxLayout( self )
        self.setLayout( self.layout )
        self.layout.setAlignment( Qt.AlignTop )

        self._modul = {}

        self._button_widget = ButtonWidget( self )
        self._perhitungan_widget = PerhitunganWidget( self )


        self.layout.addWidget( self._button_widget, 1  )
        self.layout.addWidget( self._perhitungan_widget, 5 )
        self._button_widget.adjustSize()

    def set_modul( self, list_modul : dict ):
        self._modul = list_modul

    def start( self ):
        self._button_widget.set_modul( self._modul )
        self._button_widget.adjustSize()
        self._button_widget.clicked.connect( self.change_modul )

        print( self._button_widget.size() )

    def change_modul( self ):
        pass

