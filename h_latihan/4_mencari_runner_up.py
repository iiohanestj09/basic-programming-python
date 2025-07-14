arr = list(map(int, input("Masukkan Daftar Nilai: ").split()))

newArr = list(set(arr))     #! Menghilangkan duplikasi angka dengan SET, lalu mengembalikannya dalam LIST
newArr.sort()               #! menggunakan Method SORT --> Terkecil ke Terbesar
print(f"Nilai Runner-Up: {newArr[-2]}")    #^ Mengambil Nilai Juara 2 dengan -2 (2 dari Belakang List)