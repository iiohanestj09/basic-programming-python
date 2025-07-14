## Operasi (Awalan)

# index      0(-3)    1(-2)   2(-1)
dataList = ["Maman", "Ucup", "Mario"]
print(f"List Awal = {dataList}")

# Mengambil Data dari List
print(f"Data Pertama  = {dataList[0]}")
print(f"Data Terakhir = {dataList[-1]}")

# Jumlah Data di List
print(f"Panjang Data = {len(dataList)}")


## Manipulasi List

# Menambah Item pada List Sesuai Index dan menggeser Nilai-nilai setelahnya
dataList.insert(1, "Ujang")
print(f"List Setelah Ditambah di Indeks 1 = {dataList}")

# Menambah Item di Akhir
dataList.append("Dadang")
print(f"List Setelah Ditambah di Akhir = {dataList}")

# Menambah List dengan List
dataBuffer = ["Asep", "Usep", "Osep"]
dataList.extend(dataBuffer)
print(f"List Gabungan Sekarang = {dataList}")

# Merubah Data
dataList[6] = "Michael"
print(f"Data Rubah Indeks 6 = {dataList}")

# Remove Data
dataList.remove("Mario")
print(f"Data Mario Dihapus = {dataList}")

# Remove Data Terakhir
dataList.pop()
print(f"Data Terakhir Dihapus = {dataList}")


