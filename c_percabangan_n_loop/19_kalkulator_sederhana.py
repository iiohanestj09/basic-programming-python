angka1 = float(input("Masukkan Angka (1) : "))
operator = input("Operator (+, -, *, /) : ")
angka2 = float(input("Masukkan Angka (2) : "))

if operator == "+":
    print(f"Hasil = {angka1 + angka2}")
elif operator == "-":
    print(f"Hasil = {angka1 - angka2}")
elif operator == "*":
    print(f"Hasil = {angka1 * angka2}")
elif operator == "/":
    print(f"Hasil = {angka1 / angka2}")
else:
    print("Operator Tidak Valid!")