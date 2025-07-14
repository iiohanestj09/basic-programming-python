print("List Buku Di Perpustakaan")
listBuku = []

while True:
    judulBuku = input("\nMasukkan Judul Buku   : ")
    penulis = input("Masukkan Nama Penulisnya: ")
    
    bukuBaru = [judulBuku, penulis]
    listBuku.append(bukuBaru)
    
    isLanjut = input("Ingin Menambah Buku Lagi (y untuk Iya/ Selain Itu Tidak): ")
    
    if isLanjut != "y" and "Y":
        break

print("\nBuku Sekarang Yang Ada Di Perpustakaan: ")

for index, buku in enumerate(listBuku):
    print(f"{index + 1}. {buku[0]:<15}| {buku[1]:<10}|")
