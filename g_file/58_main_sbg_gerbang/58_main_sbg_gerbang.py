# __main__ adalah top level code environment

# __name__ == '__main__'
# jika ada di-run di program utama

## __name__ pada file program utama
print(f"Nilai __name__ pada '57_main_sbg_gerbang.py' = '{__name__}'")

## __name__ pada file program eksternal (yang berisi print saja)
import contohFungsi

## contoh pengguaan __main__

# deklarasi
def fungsiTambah(a:int, b:int) -> int:
    return a + b

# fungsi utama    
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsiTambah(angka1, angka2)
    print(f"Hasil tambah = {hasil}")
    
## import package
import contohPackage
    













