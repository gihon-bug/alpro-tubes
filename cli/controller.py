from base.controller import Callable, ControllerBase, InterfacesBase, Modul
from .interfaces import InterfacesCLI
import modulfactory

class ControllerCLI( ControllerBase ):
    def __init__( self ):
        self._interfaces = []
        self._modul : Modul

    def show( self ):
        for interface in self._interfaces:
            self._modul.get_value( interface )
            interface.show_result()


    def get_modul( self ):
        i = 1
        list_modul = modulfactory.get_choice()

        for name in list_modul:
            print(f"{i}.{name}")
            i += 1
        
        while True:
            inp = input("masukkan Pilihan:")
            if inp.isdigit():
                inp = int(inp) - 1
                if inp < len(list_modul):
                    # type = modulfactory.get_type( list_modul[inp] )
                    type = 2

                    if ( type == modulfactory.ModulType.Modul ):
                        self._modul = modulfactory.get_modul( list_modul[inp] )()
                    # elif ( type == modulfactory.ModulType.Choice ):
                        # self.;;
                        
                    self.add_modul()
                    
                    break

    
    def add_modul( self ):
        interface = InterfacesCLI(self._modul.name)
        self._interfaces.append( interface )