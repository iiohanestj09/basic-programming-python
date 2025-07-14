data0 = [1, 2]
data1 = [3, 4]

data2D = [data0, data1, 7]      #? [[...], [...], 7]
data2D_copy = data2D.copy()

print(f"data2D = {data2D}")
print(f"data2D_copy = {data2D_copy}")

# Mengambil dari Nested List    #?Tambahan Materi
print(f"data2D[0][1] = {data2D[0][1]}\n")

# Address Semuanya 
print(f"Address data2D      = {hex(id(data2D))}")
print(f"Address data2D_copy = {hex(id(data2D_copy))}\n")

# Address Member 0
print("Address Member Ke-0")
print(f"Address data2D[0]      = {hex(id(data2D[0]))}")
print(f"Address data2D_copy[0] = {hex(id(data2D_copy[0]))}")

data2D[1][0] = 5
data2D[2] = 10       #! => Ganti Angka 7 yg luar sebelumnya -> [[...], [...], 10]

print(f"data2D = {data2D}")             #? [[1,2], [5,4], 10]
print(f"data2D_copy = {data2D_copy}\n")   #? [[1,2], [5,4], 7]    Beda Bagian Luarnya saja

#& Menggunakan DEEPCOPY

from copy import deepcopy
data2D_deepcopy = deepcopy(data2D)

# Address Semuanya 
print("-" * 41)
print(f"Address data2D          = {hex(id(data2D))}")
print(f"Address data2D_deepcopy = {hex(id(data2D_deepcopy))}\n")

# Address Member 0
print("Address Member Ke-0")
print(f"Address data2D[0]          = {hex(id(data2D[0]))}")
print(f"Address data2D_deepcopy[0] = {hex(id(data2D_deepcopy[0]))}\n")

data2D[1][0] = 39
print(f"data2D          = {data2D}")            # Berubah 39
print(f"data2D_copy     = {data2D_copy}")       # Berubah 39
print(f"data2D_deepcopy = {data2D_deepcopy}")   # Tetap 5