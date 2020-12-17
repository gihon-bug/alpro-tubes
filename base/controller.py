import abc

class ControllerBase( metaclass=abc.ABCMeta ):
    @abc.abstractclassmethod

    def __init__( cls ):
        pass
        
    def start(self, modul : dict ):
        pass
