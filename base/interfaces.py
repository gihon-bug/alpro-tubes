import abc
from typing import Callable

class InterfacesBase(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod

    def __init__( self, name ):
        pass
    
    def set_name( self, name ):
        pass

    def get_name( self, name ):
        pass

    def get_int( self, name, **kwargs ):
        pass

    def get_float( self, name, **kwargs ):
        pass

    def add_func( self, name, func : Callable[ [ dict ], None ], **kwargs):
        pass

    def show_result( self ):
        pass