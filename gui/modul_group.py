from PyQt5.QtWidgets import QScrollArea, QGroupBox, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from .perhitungan_widget import PerhitunganWidget

class ModulGroup( QScrollArea ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self.set_modul( None )
        self.setWidgetResizable( True )

        self.group_modul = QGroupBox( self )
        self.group_layout = QVBoxLayout( self.group_modul )
        self.group_layout.setAlignment( Qt.AlignTop )

        self.setWidget( self.group_modul )

    def set_modul( self, modul ):
        self._modul = modul

    def add_modul( self ):
        if self._modul is not None:
            modul = self._modul()
            modul_widget = PerhitunganWidget( self.group_modul, modul )
            modul_widget.setSizePolicy( QSizePolicy.Preferred , QSizePolicy.Minimum )

            self.group_layout.addWidget( modul_widget )

