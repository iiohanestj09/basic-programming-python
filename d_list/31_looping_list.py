# For Loop
print("For Loop")
dataAngka = [4, 3, 2, 5, 6, 1]
for angka in dataAngka:
    print(f"Angka = {angka}")
print(" ")

dataNama = ["Ucup", "Otong", "Dadang"]
for nama in dataNama:
    print(f"Nama = {nama}")

# For Loop dan Range
print(f"{"-" * 30}\nFor Loop dan Range")
for i in range(len(dataNama)):
    print(f"Nama = {dataNama[i]}")

# While Loop
print(f"{"-" * 30}\nWhile Loop")
i = 0
while i < len(dataAngka):
    print(f"Angka = {dataAngka[i]}")
    i += 1

# List Comperhension
print(f"{"-" * 30}\nList Comperhension")
dataAsal = ["Ucup", 1, True, 3, "Dadang"]
[print(f"Data = {i}") for i in dataAsal]

print("\n" + str([i**2 for i in dataAngka]))

# Enumerate
print(f"{"-" * 30}\nEnumerate")

for index,data in enumerate(dataAsal):
    print(f"Index = {index}\tData = {data}")
