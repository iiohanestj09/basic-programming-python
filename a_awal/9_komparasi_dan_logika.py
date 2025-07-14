print("Soal Nomor 1:\n+++++++++3_________10+++++++++")
#  +++++++++3_________10+++++++++
print("Masukkan Angka Yang Kurang Dari 3 Atau Lebih Dari 10")
pilihan1 = int(input("Pilihan 1: "))
isNomor1A = pilihan1 < 3
isNomor1B = 10 < pilihan1  
print("Apakah kurang dari 3 =", isNomor1A)
print("Apakah lebih dari 10 =", isNomor1B)
print("HASILNYA             =", isNomor1A or isNomor1B, "\n")

print("Soal Nomor 2:\n_________3+++++++++10_________")
#  _________3+++++++++10_________
print("Masukkan Angka Yang Lebih Dari 3 Dan Kurang Dari 10")
pilihan2 = int(input("Pilihan 2: "))
isNomor2A = 3 < pilihan2 
isNomor2B = pilihan2 < 10 
print("Apakah lebih dari 3   =", isNomor2A)
print("Apakah kurang dari 10 =", isNomor2B)
print("HASILNYA              =", isNomor2A and isNomor2B, "\n")

print("Soal Nomor 3:\n_________0+++++++++5_________9+++++++++16_________")
#  _________0+++++++++5_________9+++++++++16_________
print("Masukkan Angka Yang\nLebih Dari 0 Dan Kurang dari 5\nAtau\nLebih Dari 9 Dan Kurang Dari 16")
pilihan3 = int(input("Pilihan 3: "))
isNomor3A = 0 < pilihan3 
isNomor3B = pilihan3 < 5
isNomor3C = 9 < pilihan3
isNomor3D = pilihan3 < 16
print("Apakah lebih dari 0   =", isNomor3A)
print("Apakah kurang dari 5  =", isNomor3B)
print("Apakah lebih dari 9   =", isNomor3C)
print("Apakah kurang dari 16 =", isNomor3D)
print("HASILNYA              =", (isNomor3A and isNomor3B) or (isNomor3C and isNomor3D))