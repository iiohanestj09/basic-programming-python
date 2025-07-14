# Fungsi Kuadrat
def kuadrat(angka):
    hasil = angka ** 2
    return hasil

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(f"{z}\n")

# Fungsi Tambah
def tambah(angka1, angka2):
    return angka1 + angka2

a = tambah(10, 2)
print(a)

print(f"{tambah(5, 5)}\n")

def operasiMatematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    
    return tambah, kurang, kali, bagi

ta, ku, ka, ba = operasiMatematika(9, 5)
print(f"Hasil Tambah = {ta}")
print(f"Hasil Kurang = {ku}")
print(f"Hasil Kali = {ka}")
print(f"Hasil Bagi = {ba}")