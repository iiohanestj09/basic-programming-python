data_0 = [1, 2]
data_1 = [3, 4]

dataBiasa = [1, 2, 3, 4]
data2D = [data_0, data_1]
print(f"List Biasa = {dataBiasa}")
print(f"List 2D = {data2D}\n")

# Contoh Penggunaan
peserta0 = ["Ucup", 25, "Laki-laki"]
peserta1 = ["Otong", 10, "Laki-laki"]
peserta2 = ["Dedeh", 50, "Wanita"]

listPeserta = [peserta0, peserta1, peserta2]
print(f"List Peserta = {listPeserta}\n")

print("Pakai For Loop Untuk Menampilkan List 2D")
for peserta in listPeserta:
    print(f"{peserta[0]}\t{peserta[1]}\t{peserta[2]}")
    
# Dengan Reference
listCopy = listPeserta.copy()       #! List 2D ketika di-copy, dia hanya meng-copy Luarnya saja,dalam tdk
print(f"Peserta = {listCopy}\n")    #! Sehingga, ketika di ubah bagian spesifik, yg asli ikut berubah
peserta1[0] = "Michael"                   
print(f"peserta1[0] = 'Micahel'\nPeserta (listPeserta) = {listPeserta}")
print(f"Peserta (listCopy)= {listCopy}")

"""
[[...], [...],  ]
[[bkn ini], [bkn ini], ini yang dicopy]

"""
#! ==> LANJUT DI MATERI BERIKUTNYA

