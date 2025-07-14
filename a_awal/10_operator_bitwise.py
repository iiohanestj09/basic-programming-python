# Operator Bitwise, Operasi Biner, Binary
# OR, AND, XOR, NOT, SHIFTING
a = 9 
b = 5

#* Bitwise OR (|)
c = a | b
print("=======OR=======")
print("Nilai a =", a, ",  Binary :", format(a,'08b'))
print("Nilai b =", b, ",  Binary :", format(b,'08b'))
print("---------------------------------(|)")
print("Nilai c =", c, ", Binary :", format(c,'08b'), "\n")

#* Bitwise AND (&)
c = a & b
print("=======AND=======")
print("Nilai a =", a, ", Binary :", format(a,'08b'))
print("Nilai b =", b, ", Binary :", format(b,'08b'))
print("---------------------------------(&)")
print("Nilai c =", c, ", Binary :", format(c,'08b'), "\n")

#* Bitwise XOR (^)
c = a ^ b
print("=======XOR=======")
print("Nilai a =", a, ",  Binary :", format(a,'08b'))
print("Nilai b =", b, ",  Binary :", format(b,'08b'))
print("---------------------------------(^)")
print("Nilai c =", c, ", Binary :", format(c,'08b'), "\n")

#* Bitwise NOT (~)
#! ==> ~x = -(x + 1)
c = ~a
print("=======NOT=======")
print("Nilai a =", a, ",   Binary :", format(a,'08b'))
print("---------------------------------(~)")
print("Nilai c =", c, ", Binary :", format(c,'08b'), "\n")

#* SHIFT RIGHT
c = b >> 2
print("========SHIFT RIGHT========")
print("Nilai b =", b, ", Binary :", format(b,'08b'))
print("---------------------------------(>>)")
print("Nilai c =", c, ", Binary :", format(c,'08b'), "\n")

#* SHIFT LEFT
c = b << 3
print("========SHIFT LEFT========")
print("Nilai b =", b, ",  Binary :", format(b,'08b'))
print("---------------------------------(<<)")
print("Nilai c =", c, ", Binary :", format(c,'08b'), "\n")