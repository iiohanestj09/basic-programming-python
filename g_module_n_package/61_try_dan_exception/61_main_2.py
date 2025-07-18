# Contoh Membuat Exception

from numbers import Number

# Contoh 1:
def tambah(a,b):
    notA = isinstance(a,Number)
    notB = isinstance(b,Number)
    
    if notA == False and notB == False:
        raise "Input Kedua-duanya Harus Angka!"
    elif notA == False and notB == True:
        raise "Input Pertama Harus Angka!"
    elif notA == True and notB == False:
        raise "Input Kedua Harus Angka"
    
    return a + b

print(tambah(5,6))

## Contoh 2:
angka = 0

try:
    hasil = 10/angka
except Exception as pesanError:         # Lebih Gampang
    print(pesanError)                   # --> "division by zero"

        