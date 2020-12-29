from PyQt5.QtWidgets import QLineEdit

class LineEdit( QLineEdit ):
    def __init__( self, name, parent=None ):
        super().__init__( "" , parent )
        self._name = name
    
    def get_name( self ):
        return self._name
