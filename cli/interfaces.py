from base.interfaces import InterfacesBase
from typing import Callable

class InterfacesCLI(InterfacesBase):
    def __init__( self, name ):
        self.set_name(name)
        self._value = {}
        self._result = {}
        self._list_get_value = {}
    
    def set_name( self, name ):
        self._name = name

    def get_name( self ):
        return self._name

    def _get_value( self, name, **kwargs  ):
        if "kwargs" in kwargs:
            kwargs = kwargs["kwargs"]

        func = lambda text : text 
        if "func" in kwargs:
            func = kwargs["func"]
        
        input_warning = f"masukkan nilai {name}: "
        if "inpur_warning" in kwargs:
            input_warning = kwargs["input_warning"]
        
        error_warning = ""
        if "error_warning" in kwargs:
            error_warning = kwargs["error_warning"]
        
        try:
            self._value[name] = func( input(input_warning) )
        except ValueError:
            print(error_warning)
            return self._get_value( name, kwargs=kwargs )
        
    def _add_getter( self, name, kwargs : dict ):
        if not "func" in kwargs:
            kwargs["func"] = lambda text : text

        if not "input_warning" in kwargs:
            kwargs["input_warning"] = f"masukkan nilai {name}:"
        
        if not "error_warning" in kwargs:
            kwargs["error_warning"] = "tidak bisa menkonversi input yang dilakukan"

        self._list_get_value[name] = {
            "func" : kwargs["func"],
            "input_warning" : kwargs["input_warning"],
            "error_warning" : kwargs["error_warning"]
        }

    def get_int( self, name, **kwargs ): 
        kwargs["func"] = lambda inp:int(inp)

        if not "error_warning" in kwargs:
            kwargs["error_warning"] = "hanya masukkan nilai angka"

        self._add_getter( name, kwargs )
        
    def get_float( self, name, **kwargs ):

        kwargs["func"] = lambda inp:float(inp)

        if not "error_warning" in kwargs:
            kwargs["error_warning"] = "hanya masukkan nilai angka, pisahkan desimal dengan \".\" (Titik)"
        
        self._add_getter( name,kwargs )

    def add_func( self, name, func : Callable[ [ dict ], None ] ):
        if not name in self._result:
            self._result[name] = []

        self._result[name].append( func )

    def show_result( self ):
        for name, val in self._list_get_value.items():
            self._get_value( name, kwargs=val )
        for name, val in self._result.items():
            self._value["_name"] = name
            for func in val:
                print(f"{name} = { func(self._value) }")
