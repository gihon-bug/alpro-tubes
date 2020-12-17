from base.modul import Modul
from fisdas.vektor import Vektor
from fisdas.menara_air import MenaraAir

class ModulType:
    Choice = 1
    Modul = 2

# ini buat list modulnya
# langsung masukin sini aja
list_modul = {
    Vektor.name : Vektor,
    MenaraAir.name : MenaraAir
}

def get_all_modul() -> list:
    return list_modul


def get_type( key : str ):
    if issubclass( list_modul[key], Modul ):
        return ModulType.Modul

    elif list_modul[key] is dict:
        return ModulType.Choice
    
def get_modul( key : str ) -> Modul:
    return list_modul.get(key)
