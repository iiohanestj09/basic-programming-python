def fungsi(nama, tinggi, berat):        #? Param-nya harus ketik satu-satu
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Ucup", 170, 40)

def fungsi(dataList):
    dataX = dataList.copy()
    nama = dataX[0]
    tinggi = dataX[1]
    berat = dataX[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["Otong", 100, 120])     #? Harus Ngetik [ ]-nya, kalau kelupaan, error

# Penggunaan *args
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Dudung", 120, 120)

def tambah(*data):
    varX = 0
    for angka in data:
        varX += angka
    
    return varX

print(f"\nHasil = {tambah(1,2,3,4,5,6,7,8,9)}")
print(f"Hasil = {tambah(10,5,15)}")