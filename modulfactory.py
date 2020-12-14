from base.modul import Modul
from fisdas.vektor import Vektor

class ModulType:
    Choice = 1
    Modul = 2

list_modul = {
    "Vektor" : Vektor
}

def get_choice() -> list:
    li = []
    for i in list_modul.keys():
        li.append( i )
    return li


def get_type( key : str ):
    if issubclass( list_modul[key], Modul ):
        return ModulType.Modul

    elif list_modul[key] is dict:
        return ModulType.Choice
    
def get_modul( key : str ) -> Modul:
    return list_modul.get(key)