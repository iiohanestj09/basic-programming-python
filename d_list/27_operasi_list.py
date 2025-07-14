dataAngka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 9, 8, 0]
print(f"Data Angka = {dataAngka}")

# Count data
print(f"Banyaknya Angka 4 = {dataAngka.count(4)}")
print(f"Banyaknya Angka 3 = {dataAngka.count(3)}\n")

dataNama = ["Ucup", "Otong", "Dudung", "Ujang"]
print(f"Data Nama = {dataNama}")

# Ambil Posisi Index
print(f"'Dudung' Berada di Indeks Ke-{dataNama.index("Dudung")}")
print(f"'Ujang' Berada di Indeks Ke-{dataNama.index("Ujang")}\n")

# Mengurutkan List
#! .sort() == Metode
#! sorted() == Fungsi --> Tidak menghilangkan Iterable Asli

dataAngka.sort()
print(f"Data Angka Setelah Di-Sort = {dataAngka}")

dataNama.sort()
print(f"Data Nama Setelah Di-Sort = {dataNama}\n")

# Membalik Urutan List
dataAngka.reverse()
print(f"Data Angka Setelah Di-Reverse = {dataAngka}")

