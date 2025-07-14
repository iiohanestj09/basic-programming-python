def sayHello(nama = "Ganteng"):
    print(f"Hello {nama}")

sayHello("Ucup")
sayHello()
print("-" * 20)

def sapaDia(nama, pesan = "Apa Kabar"):
    print(f"Hai {nama}, {pesan}")

sapaDia("Dudung", "Hai Ganteng")
sapaDia("Otong")
print("-" * 20)

def hitungPangkat(angka, pangkat = 2):
    hasil = angka ** pangkat
    return hasil

print(hitungPangkat(2, 4))
hasilX = hitungPangkat(pangkat = 3, angka = 5)
print(hasilX)
print("-" * 20)

def fungsi(input1 = 2, input2 = 2, input3 = 3, input4 = 4):
    return  input1 + input2 + input3 + input4

print(fungsi())
print(fungsi(input3 = 1))    