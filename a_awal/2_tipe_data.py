# Tipe Data Normal Di Python
dataString = "Yohanes Putra P. Muwa Dae"
dataInteger = 19
dataFloat = 3.94
dataBool = True 
dataList = [1, 2.9, "ayam"]

print("Nama Saya :", dataString, "\n", type(dataString), "\n")
print("Umur Saya :", dataInteger, "\n", type(dataInteger), "\n")
print("IPS 1 Saya:", dataFloat, "\n", type(dataFloat), "\n")
print("Saya Lulus:", dataBool, "\n", type(dataBool), "\n")
print("Contoh:", dataList, "\n", type(dataList), "\n")

#! Tipe Data Khusus
# Bilangan kompleks (Real dan Imajiner)
# Bilangan imajiner itu √-1 = i
dataComplex = complex(5,6)          #? ==> 5 + 6i -->     5 + (√36 * √-1)     --> 5 + √-36
print("Bilangan Kompleks:", dataComplex, "\n", type(dataComplex), "\n")

# Tipe Data Dari C
import ctypes

dataDouble = ctypes.c_double(0.001)
dataChar = ctypes.c_char(b'z')             #? Konversi ke Byte string
dataLong = ctypes.c_long(10101010101)
dataShort = ctypes.c_short(12345)

print("Data Double:", dataDouble.value, "\n", type(dataDouble), "\n")     #* Penambahan .value
print("Data Char  :", dataChar.value, "\n", type(dataChar), "\n")       
print("Data Long  :", dataLong.value, "\n", type(dataLong), "\n")
print("Data Short :", dataShort.value, "\n", type(dataShort))

# Bisa juga beberapa Tipe data Integer yang lebih Eksplisit seperti c_int8, c_uint8