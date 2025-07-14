import os

def header():
    os.system("cls")
    print(f"Menghtiung Luas dan Keliling Persegi Panjang")
    print("-"*44)

def inputUser():
    panjang = int(input("Masukkan Nilai Panjang: "))
    lebar = int(input("Masukkan Nilai Lebar: "))
    return lebar, panjang

def hitungLuas(panjang, lebar):
    return panjang * lebar

def hitungKeliling(panjang, lebar):
    return 2 * (panjang + lebar)

def tampil(operasi, nilai):
    print(f"Hasil Perhtungan {operasi} = {nilai}")
    
# Program Utamanya
while True:
    header()
    panjang, lebar = inputUser()
    
    tampil("Luas", hitungLuas(panjang, lebar))
    tampil("Keliling", hitungKeliling(panjang, lebar))
    
    isLanjut = input("Apakah Ingin Lanjut(y/n): ")
    
    if isLanjut == "n":
        break