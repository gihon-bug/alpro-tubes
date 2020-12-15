from base.controller import Callable, ControllerBase, InterfacesBase, Modul
from .interfaces import InterfacesCLI
import modulfactory

class ControllerCLI( ControllerBase ):
    def __init__( self ):
        self._interfaces = InterfacesCLI("")
        self._modul : Modul

    def show( self ):
        self._interfaces.show_result()

    def get_modul( self, modul : dict ):
        inp = ""

        keys : list = []
        for key in modul.keys():
            keys.append( key )

        while inp != "0":
            i = 1

            for name in keys:
                print(f"{i}.{name}")
                i += 1
            print("0.Exit")
            
            inp = input("masukkan Pilihan:")
            if inp.isdigit():
                idx = int(inp) - 1
                if idx >= 0 and idx < len( keys ):
                    modul_name = keys[idx]

                    if issubclass( modul[modul_name], Modul ):
                        type = modulfactory.ModulType.Modul
                    elif modul[modul_name] is dict:
                        type = modulfactory.ModulType.Choice

                    if ( type == modulfactory.ModulType.Modul ):
                        self._modul = modulfactory.get_modul( keys[idx] )()
                        self.add_modul()
                        self.show()

                    elif ( type == modulfactory.ModulType.Choice ):
                        self.get_modul( modul[ keys[idx] ] )
                            
    def add_modul( self ):
        interface = InterfacesCLI(self._modul.name)
        self._modul.get_value( interface )
        self._interfaces = interface