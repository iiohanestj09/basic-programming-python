
#* Pass ==> Sebagai Dummy, Tidak Akan Dieksekusi, hanya sebagai penanda
angka = 0
while angka < 5:
    print(f"Angka Sekarang --> {angka}")
    
    if angka == 3:
        pass
    
    angka += 1
print("Selesai (1)\n")

#* Continue ==> Akan Melanjutkan/Melompat ke Iterasi Berikutnya dan mengabaikan program di bawahnya
angka = 0
while angka < 5:
    angka += 1    
    print(f"Angka Sekarang --> {angka}")
    
    if angka == 3:
        print("NICEEEEEEEEE!")
        continue

    print("Wassup")
print("Selesai (2)\n")

#* Break ==> Menghentikan Looping 
#* a
angka = 0
while angka < 5:
    angka += 1
    print(f"Angka Sekarang --> {angka}")
    if angka == 3:
        print("Mantabbb!")
        break
    
    print("Holaaa")
print("Selesai (3)\n")

#* b
batas = int(input("Masukkan Batas Loop (dari 1) : "))
angka = 0

while True:
    angka += 1
    print(f"Count = {angka}")
    
    if angka == batas:
        print("SIAP, SELESAI")
        break
    
    print("Siap")
