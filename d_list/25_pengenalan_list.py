
#* Macam - Macam List
# Kumpulan Data Numbers
dataAngka = [1, -2, 5, 3, -1, 9, 8.2, 7.3, -11.5]
print(dataAngka)

# Kumpulan Data String
dataString = ["Maman", "Ucup", "Mario", "Maria"]
print(dataString)

# Kumpulan Data Boolean
dataBoolean = [True, False, True, True]
print(dataBoolean)

# Data Campuran 
dataCampuran = ["Maman", 19, "Ucup", -5, "Mario", False, True]
print(dataCampuran)

#^ Cara Alternatif Membuat List
# Pakai Range
dataRange = list(range(0, 10, 2))  #range(START, STOP, STEP)
print(dataRange)

# Pakai For Loop, List Comperhension
dataFor = [i**2 for i in range(0, 15, 3)]
print(dataFor)

# Pakai For Loop dan If
dataForIf = [i for i in range(0, 7) if i != 2 and i != 5]
print(dataForIf)

dataForIf = [i**2 for i in range (0, 6) if i % 2 == 0]
print(dataForIf)


