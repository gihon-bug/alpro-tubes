import abc
from base.interfaces import InterfacesBase

class Modul( metaclass=abc.ABCMeta ):
    name = ""
    @abc.abstractclassmethod

    def get_value( self, input : InterfacesBase ):
        pass

    def show( self ):
        pass