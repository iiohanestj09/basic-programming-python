
#* For Looping dengan Range
for i in range(5):
    print(f"{i} Halo Dunia")
print("==> AKHIR DARI PROGRAM 1\n")

#* For Looping dengan Range yang Ditentukan
for i in range(11, 16):                     #! range(x,y) ==> x, x+1, x+2, ..., y-1
    print(f"Angka Sekarang --> {i}")
print("==> AKHIR DARI PROGRAM 2\n")

#* For Looping dengan Variabel
varRange = range(2, 7)                      #! range(2,7) ==> 2, 3, 4, 5, 6
for i in varRange:
    print(f"Angka Sekarang --> {i}")
print("==> AKHIR DARI PROGRAM 3\n")

#* For Looping dengan List
angka2 = [17, 9, 22, 3, 14]
for i in angka2:
    print(f"Angka Sekarang ==> {i}")
print("==> AKHIR DARI PROGRAM 4\n")
