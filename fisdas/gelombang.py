import math
from base.interfaces import InterfacesBase
from base.modul import Modul

# kalo mau buat kelas(Modul) baru
# ini filenya dicopy terus ganti nama
# "Vektor"nya diganti
# "Moduil"nya jangan
# kalo udah jadi, masukkin ke file modulfactory.py
class Gelombang( Modul ):
    # ini nama praktikumnya
    name = "Gelombang"

    # ini tempat ngambil nilai
    def get_value( self, interfaces : InterfacesBase ):
        # kalo mau minta bilangan bulat pake get_int
        # kalo minta bilangan desimal pake get_float
        # parameter pertama itu buat namain variablenya pas nanti dioper
        # kalo make parameter yang sama, nanti ke overwrite jadi hati hati
        interfaces.get_float("s")
        interfaces.get_float("n")
        interfaces.get_float("lamda")
        interfaces.get_float("f")

        # ini buat nambahin fungsi buat ngitung rumusnya,
        # parameter pertama itu hasil dari apa,
        # parameter kedua itu fungsinya
        # ini bisa dipanggil berkali-kali
        interfaces.add_func("Panjang gelombang seluruhnya / Jumlah gelombang yang terukur (s/n)", self.menentukan_panjang_gelombang)
        interfaces.add_func("lamda * Frekuensi", self.menentukan_cepat_rambat_gelombang)


    # ini fungsi buat ngitung rumusnya
    # parameter kedua itu buat nilai yang diambil dari method
    # get_value diatas
    # isi key( [key] ) itu sama kayak yang parameter diatas
    # kalo diatas interfaces.get_float("a")
    # ngambilnya value["a"]

    # kalo mau ngambil nama yang dimasukkin
    # di add_func parameter pertama
    # bisa ngambil lewat value["_name"]
    def menentukan_panjang_gelombang( self, value : dict ):
        s = value["s"]
        n = value["n"]
        return str(math.sqrt(s/n))
    def menentukan_cepat_rambat_gelombang(self, value : dict):
        lamda = value["lamda"]
        f = value["f"]
        return str(math.sqrt(lamda*f))