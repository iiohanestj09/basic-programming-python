# Exception akan terjadi saat program 
# mengalami error saat runtime

# contoh sederhana untuk menangkap exception

from math import nan        #! nan == not a number

##^ Contoh Sederhana
# inputUser = int(input("Masukkan Angka Pembagi: "))
# hasil = nan

# try:
#     hasil = 10/inputUser
# except:
#     print("INPUT TIDAK BOLEH 0")
    
# print(f"Hasil = {hasil}")

##^ Contoh Di Aplikasi 
while True:
    angka = int(input("Masukkan Angka Pembagi: "))
    try:
        hasilX = 10/angka
        print(f"Hasil = {hasilX}")
        isDone = input("Lanjutkan (y/n): ")
        
        if isDone == "n":
            break
    except:
        print("PEMBAGI 0\nSILAHKAN MASUKKAN INPUT LAGI!")


print("Akhir dari Program 1\n")

## Contoh Aplikasi Untuk Membuat File data.txt
try:
    with open("data.txt", 'r') as berkas:
        print("File 'data.txt' Ditemukan\nMembaca File")
        print(berkas.read())
except:
    print("File 'data.txt' Tidak Ditemukan\nMembuat File Baru")
    with open("data.txt", 'w', encoding='utf-8') as berkas:
        berkas.write("File Baru-Baris Pertama")

print("Akhir dari Program 2")