# List
dataList = [10, 4, 3, 2]
print(f"dataList = {dataList}")

# Tuples    ==> Konstan, Nilai-Nilai didalamnya tidak bisa dimanipulasi
dataTuples = (1, 7, 8, 0, -6, 100, -3, 5, 1)
print(f"dataTuples = {dataTuples}")

# Tidak Bisa Dilakukan
# dataTuples[1] = 16
# dataTuples.append(1)

# Sets      ==> Urutan Tidak Berlaku, karena BEBERAPA KONDISI SUDAH TERURUT (TIDAK KONSISTEN). Selebihnya mirip-mirip dengan List
dataSets = {10, 4, 3, 2, 4, 7, 6, 5}
print(f"dataSets = {dataSets}")

# Tidak Bisa Dilakukan ==> print(dataSets[0])

# ┌────────────┬──────────┬────────────┬─────────────────┬────────────────────────────────────────────────────────┐
# │ Tipe       │ Urutan   │ Mutable    │ Elemen Duplikat │ Kegunaan Umum                                          │
# ├────────────┼──────────┼────────────┼─────────────────┼────────────────────────────────────────────────────────┤
# │ list       │ Ya       │ Ya         │ Ya              │ Menyimpan data terurut yang bisa diubah                │
# │ tuple      │ Ya       │ Tidak      │ Ya              │ Menyimpan data terurut yang tetap (konstan)            │
# │ set        │ Tidak    │ Ya         │ Tidak           │ Kumpulan data unik (tidak terurut), Operasi Himpunan   │ 
# └────────────┴──────────┴────────────┴─────────────────┴────────────────────────────────────────────────────────┘
