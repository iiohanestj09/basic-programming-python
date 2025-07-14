## Variabel Global Scope
nama_global = "otong"   # <-- Ini Variabel Global

# Akses Variabel Global dalam Fungsi
def fungsi1():
    print(f"Fungsi Menampilkan {nama_global}\n")

fungsi1()

# Akses Variabel Global dalam Loop
for i in range(0,5):
    print(f"{i} - {nama_global}")

# Akses Variabel Global dalam Percabangan
if True:
    print(f"\nIf Menampilkan {nama_global}\n")


## Variabel Local Scope
def fungsi2():
    nama_local = "ucup"  # <-- Ini Variabel Local 
    print(f"{nama_local}\n")

fungsi2()

## Contoh 1: Penggunaan
def sayDudung():
    print(f"Hello {nama}")

nama = "Dudung"
sayDudung()

## Contoh 2: Merubah Variabel Global di Fungsi
angka = 0
nama = "Mario"

def ubah(nilaiBaru, namaBaru):
    global angka            #! Menggunakan global
    global nama
    
    angka = nilaiBaru
    nama = namaBaru

print(f"Sebelum, {angka, nama}")
ubah(10, "Asep")
print(f"Sesudah, {angka, nama}")

## Contoh 3:
number = 0

for i in range(0, 3):
    number += i          # Variabel Global
    numberDummy = 18     # Variabel Local

print(number)       
print(numberDummy)

