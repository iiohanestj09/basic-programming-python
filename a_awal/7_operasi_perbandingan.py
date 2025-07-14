# Operasi Perbandingan atau Komparasi di Python:
# <, >, <=, >=, ==, !=, is, is not
print("Kurang Dari, 5 < 6 =", 5 < 6)
print("Lebih Dari , 5 > 6 =", 5 > 6, "\n")
print("Kurang Dari Sama Dengan, -3 <= 3 =", -3 <= 3)
print("lebih Dari Sama Dengan , 3 >= 4 =", 3 >= 4, "\n")
print("Sama Dengan      , 2 == 2 =", 2 == 2)
print("Tidak Sama Dengan, 2 != 2 =", 2 != 2, "\n")

#* Is dan Is Not Membandingkan Berdasarkan 'Alamat Memori kedua Variabel'
a = 9
b = 8
c = 10
d = 10
e = a
f = [1, 2, 3, 4]
g = [1, 2, 3, 4]
h = False
i = False

print("Is    , a is b =", a is b)
print("Is    , c is d =", c is d)       
# Hasilnya True walau nilai sama, Python melakukan optimisasi internal == Interning
# Sehingga, d akan menunjuk ke objek yang sama dengan c, yaitu 10
# Alih-alih membuat objek baru. Makanya alamat keduanya SAMA

print("Is    , a is e =", a is e)       
print("Is    , f is g =", f is g)       
print("Is    , h is i =", h is i)
print("Is Not, a is not b =", a is not b)
print("Is Not, c is not d =", c is not d)


