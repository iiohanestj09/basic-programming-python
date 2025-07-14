# Operasi Dan Manipulasi String (PART2)

#* 4. Operator Dalam Bentuk Method

#* 4.1 Menghitung Banyaknya char/string pada sebuah String {.count()}
data = "otong surotong pararotong"
jumlaho = data.count("o")
print("Banyaknya Huruf 'o' pada " + data + " = " + str(jumlaho))

jumlahro = data.count("oto")
print('Banyaknya Kata "oto" pada ' + data + " = " + str(jumlahro) + "\n")

#* 4.2 Merubah Case dari String {.upper(), .lower()}
salam = "SeLaMaT PaGi GuYs!"
print("Normal = " + salam)
print("Upper = " + salam.upper())
print("Lower = " + salam.lower() + "\n")

#* 4.3 Pengecekan dengan isX Method {.islower(), isupper()}
salam = "haloooo"
print("Apakah " + salam + " Lower = " + str(salam.islower()))
print("Apakah " + salam + " Upper = " + str(salam.isupper()))

#? .isalpha()   <-- Untuk mengecek semuanya Huruf
#? .isalnum()   <-- Untuk mengecek Huruf dan angka (alpha & number)
#? .isdecimal() <-- Untuk mengecek semuanya Angka
#? .isspace()   <-- Spasi, Tab, Newline
#? .istitle()   <-- Semua Kata diawali dengan huruf besar

judul1 = "Marriage Not Dating"
judul2 = "It's Different"         #! ==> It's == It is, jadi bukan title ++ Aturan Judul tidak pakai '
print(judul1 + " Merupakan Title = " + str(judul1.istitle()))
print(judul2 + " Merupakan Title = " + str(judul2.istitle()) + "\n")

#* 4.4 Mengecek Komponen {.startswith(), .endswith()}
print("Anyeong Sajangnim Oppa")
cekStarts = "Anyeong Sajangnim Oppa".startswith("anyeong")
cekEnds = "Anyeong Sajangnim Oppa".endswith("Oppa")
print("Starts 'anyeong' = " + str(cekStarts))
print("Ends 'Oppa' = " + str(cekEnds) + "\n")

#* 4.5 Penggabungan Komponen {.join(), .split()}
contohList = ["Aku", "Sayang", "Kamu"]
print(",".join(contohList))
print(" ".join(contohList))

contohList = "AkuehmSayangehmKamu"
print(contohList.split("ehm"))
print(contohList)

#* 4.6 Alokasi Karakter {.rjust(), .ljust(), .center()}
kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(6)
print("'" + kiri + "'")

tengah1 = "tengah1".center(15)
print("'" + tengah1 + "'")

print("'" + "tengah2".center(20,"=") + "'" + "\n")

#*  Kebalikannya --> {.strip()}
tengah2 = "tengah2".center(20,"@")
print("Sebelum = " + "'" + tengah2 + "'")
print("Sesudah = " + "'" + tengah2.strip("@") + "'")