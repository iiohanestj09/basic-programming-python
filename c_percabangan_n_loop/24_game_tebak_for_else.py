import random

print("SELAMAT DATANG DI GAME TEBAK NOMOR!")
print("#Pilih Tingkat Kesulitan")
print("1. Easy : 10 kali kesempatan")
print("2. Hard : 5  kali kesempatan")

while True:
    pilihan = input("Masukkan Pilihan Anda : ")
    if pilihan == "1":
        kesempatan = 10
        break
    elif pilihan == "2":
        kesempatan = 5
        break
    else:
        print("Pilihan Tidak Valid, Coba Lagi!")
        
nomorRahasia = random.randint(1, 100)

for i in range(kesempatan):
    while True:
        try:
            tebakan = int(input(f"Tebakan {i+1}: "))
            if 1 <= tebakan <= 100:
                break
            else:
                print("Tebakan Harus Antara 1 Sampai 100!")
        except ValueError:
            print("Masukkan Angka Yang Valid!")
            
    if tebakan < nomorRahasia:
        print("Tebakan Anda Terlalu Rendah!")
    elif tebakan > nomorRahasia:
        print("Tebakan Anda Terlalu Tinggi!")
    else:
        print(f"Selamat! Anda Berhasil Menebak Nomor Rahasia {nomorRahasia}")
        print(f"Dalam {i+1} Kali Percobaan ^-^ ")
        break
else:
    print(f"Kesempatan Habis. Nomor Rahasianya Adalah {nomorRahasia}. Semoga Beruntung Lain Kali")
    
"""
! Bagian ELSE yang terletak di bawah blok FOR digunakan untuk menjalankan kode setelah
    ! loop FOR selesai berjalan tanpa adanya BREAK. 

^ Ini adalah fitur yang unik dalam Python di mana blok ELSE bisa digunakan dengan FOR dan WHILE.
"""