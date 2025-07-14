# NOT, OR, AND, XOR
a = True
b = False
c = True 
d = False
y = not b

#* NOT  (Negasi Dari A Nilai Bool)
print("#NOT\nNilai a     =", a)
print("Nilai not a =", not a)
print("Nilai b     =", b)
print("Nilai not b =", y, "\n")

#* OR   (Dari 2 Nilai, Jika Salah Satu Saja True, Maka Hasilnya True)
print(f"#OR\n{a} OR {b}  = {a or b}")
print(a, "OR", c, "  =", a or c)
print(b, "OR", c, " =", b or c)
print(b, "OR", d, "=", b or d, "\n")

#* AND  (Dari 2 Nilai, Jika Keduanya True, Maka Hasilnya True)
print(f"#AND\n{a} AND {b}  = {a and b}")
print(a, "AND", c, "  =", a and c)
print(b, "AND", c, " =", b and c)
print(b, "AND", d, "=", b and d, "\n")

#* XOR (^)  (Dari 2 Nilai, Jika Kedua Nilai BERBEDA, Maka True)
print(f"#XOR\n{a} XOR {b}  = {a ^ b}")
print(a, "XOR", c, "  =", a ^ c)
print(b, "XOR", c, " =", b ^ c)
print(b, "XOR", d, "=", b ^ d)