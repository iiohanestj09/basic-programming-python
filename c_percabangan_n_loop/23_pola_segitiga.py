
#* Menggunakan For Loop
baris = 5
kolom = 1
for i in range(baris):
    print("*" * kolom)
    kolom += 1
print("Selesai (1)\n")

#* Menggunakan While Loop
kolom = 1
while True:
    print("*" * kolom)
    
    if kolom > baris:
        break
    
    kolom += 1
print("Selesai (2)\n")

#* Segitiga Piramida Dengan Lubang-lubang
kolom = 1
spasi = baris - 1
for i in range(baris):
    print(" " * spasi + "* " * kolom)
    kolom += 1
    spasi -= 1
print("Selesai (3)\n")

#* Segitiga Piramida Full
baris = 10
kolom = 1
spasi = int(baris / 2)
for i in range(baris):
    if kolom % 2 == 0:
        kolom += 1
        continue
    
    print(" " * spasi + "*" * kolom)
    kolom += 1
    spasi -= 1
print("Selesai (4)")