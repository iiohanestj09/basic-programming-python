# Penggunaan f""

#* String
nama = "Maman"
formatStr = f"Hello {nama}"
print(formatStr)

print(f"Goode Morninge {nama}\n")

#* Integer
angkaInt = 98765
formatInt = f"Angka Int = {angkaInt}"
print(formatInt)

print(f"Terdapat Sebuah Angka Yaitu {angkaInt}\n")

#* Boolean
truMin = True
formatBool = f"Tru Min? {truMin}"
print(formatBool)

print(f"Affah Iyah? {truMin}\n")

#^ Format-format Angka 
#^ 1. Menampilkan Tanda + dan -
angkaPlus = 10
angkaMinus = -10
print(f"Plus  = {angkaPlus:+}")
print(f"Minus = {angkaMinus:+}\n")

#^ 2. Angka Desimal {Mengambil Banyaknya Koma Saja, Leading Zero}
angkaFloat = 2005.54321
formatFloat = f"Angka Float = {angkaFloat:.2f}"     #! :.2f == mengambil 2 belakang koma
print(formatFloat)
formatFloat = f"Angka Float dengan Leading Zero = {angkaFloat:010.2f}\n"  
                            #! 010 == 0 leading zero, 10 banyaknya angka keseluruhan
print(formatFloat)

#^ 3. Persen
persen1 = 0.045
persen2 = 0.8
print(f"Angka 1 = {persen1}, Format Persennya = {persen1:.2%}")
print(f"Angka 2 = {persen2}, Format Persennya = {persen2:.0%}\n")

#^ 4. Operasi Aritmatika Di Dalam Placeholder + Menunjukan Koma Sebagai Ribuan/Jutaan dll
harga = 10000
jumlah = 500
print(f"Diketahui: Harga = {harga} dengan jumlah {jumlah}, maka totalnya = {(harga * jumlah):,}\n")

#^ 5. Format Bilangan Lainnya (Binary, Octal, Hexadecimal)
bilangan = 255
print(f"Bilangan    = {bilangan}")
print(f"Binary      = {bin(bilangan)}")
print(f"Octal       = {oct(bilangan)}")
print(f"Hexadecimal = {hex(bilangan)}")
