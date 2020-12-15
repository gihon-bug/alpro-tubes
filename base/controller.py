import abc
from typing import Callable
from .modul import Modul
from .interfaces import InterfacesBase

class ControllerBase( metaclass=abc.ABCMeta ):
    @abc.abstractclassmethod

    def __init__( self ):
        pass
        
    def get_modul(self, modul : dict ):
        pass