# Fungsi Biasa
def fungsi(nama, tinggi, berat):
    print(f"{nama} Punya Tinggi {tinggi} dan Berat {berat}")

fungsi("Ucup", 183, 79)

# Fungsi Dengan **kwargs
def fungsi(**kwargs):
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"{nama} Punya Tinggi {tinggi} dan Berat {berat}")

fungsi(nama = "Ucup", tinggi = 183, berat = 79)

# Studi Kasus
def matematika(*args, **kwargs):
    if kwargs['option'] == "tambah":
        varX = 0
        for angka in args:
            varX += angka
    elif kwargs['option'] == "kali":
        varX = 1
        for angka in args:
            varX *= angka
    else:
        print("Tidak Ada Operasi")
    
    return varX

print(matematika(1, 2, 3, 4, option = "tambah"))

hasil = matematika(1, 2, 3, 4, option = "kali")
print(hasil)