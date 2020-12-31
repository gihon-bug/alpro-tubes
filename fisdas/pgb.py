from base.interfaces import InterfacesBase
from base.modul import Modul
import math

class PGB( Modul ):
    name = "Percepatan Gravitasi Bumi"

    def get_value( self, interfaces : InterfacesBase ):
        interfaces.get_float("l")
        interfaces.get_float("t")
        interfaces.add_func("Periode", self.periode_getaran )
        interfaces.add_func("g",self.percepatan_gravitasi_bumi)

    def periode_getaran( self, value : dict ):
        t = value ["t"]
        n = value ["n"]

        periode = n/t
        return periode

    def percepatan_gravitasi_bumi(self,value : dict):
        l = value ["l"]
        n = value ["n"]
        t = value ["t"]

        g = (4*(math.pi ** 2)*l) / (n/t) ** 2
        return g