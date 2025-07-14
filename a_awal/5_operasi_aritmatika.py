a = 10
b = 3

"""
    Prioritas Aritmatika:
    - ()
    - *, /, %, **, //
    - +, - 
    
"""

#* Penjumlahan
print(a, "+", b, "=", a + b)

#* Pengurangan
print(a, "-", b, "=", a - b)

#& Perkalian
print(a, "*", b, "=", a * b)

#& Pembagian
print(a, "/", b, "=", a / b)    #? OTOMATIS Ke FLOAT, baik Habis Bagi ataupun Sisa Bagi

#^ Modulus
print(a, "%", b, "=", a % b)

#^ Eksponen
print(a, "**", b, "=", a ** b)

#^ Floor Division  --> Pembagian yang hasilnya dibulatkan ke bawah
print(a, "//", b, "=", a // b, "\n")

hasil1 = a ** b - b * a + b % a / a // a
print("Hasil 1 =", hasil1)

# a ** b - b * a + b % a / a // a
# 1000 - 30 + 3 % 10 / 10 // 10
# 1000 - 30 + 3 / 10 // 10
# 1000 - 30 + 0.3 // 10
# 1000 - 30 + 0.0
# 970.0

hasil2 = a ** ((b - b) * (a + b)) % b / a // a
print("Hasil 2 =", hasil2)

# a ** ((b - b) * (a + b)) % b / a // a
# 10 ** (0 * 13) % 3 / 10 // 10
# 10 ** 0 % 3 / 10 // 10
# 1 % 3 / 10 // 10            #! a % b, jika 'a < b', maka a % b = a
# 3 / 10 // 10
# 0.3 // 10
# 0.0
                