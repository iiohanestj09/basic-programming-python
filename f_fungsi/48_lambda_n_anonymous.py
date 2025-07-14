# Fungsi Biasa 
def fungsiKuadrat(angka):
    return angka**2

print(f"Hasil Fungsi Biasa Kuadrat : {fungsiKuadrat(3)} ")

# Menggunakan Lambda 
# output = lambda argument : expression
kuadrat = lambda angka : angka**2
print(f"Hasil Lambda Kudarat : {kuadrat(3)}")

pangkat = lambda basis,eksponen : basis**eksponen
print(f"Hasil Lambda Pangkat : {pangkat(5,2)}\n")

#* Kegunaan Lambda
    # Sorting 
# Sorting Panjang untuk list biasa
dataList = ["Otong", "Ucup", "Dudung"]

def panjangNama(nama):
    return len(nama)

dataList.sort(key= panjangNama)
print(f"Sorting Panjang Nama Biasa : {dataList}")

#  Menggunakan Lambda
dataList = ["Otong", "Ucup", "Dudung"]

dataList.sort(key= lambda nama: len(nama))
print(f"Sorting Panjang Nama Lambda : {dataList}\n")

    # Filter
dataAngka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurangDariLima(angka):
    return angka < 5

dataAngka_baru = list(filter(kurangDariLima, dataAngka))
print(f"Filter Biasa : {dataAngka_baru}")

print(f"Filter Lambda(1) : {list(filter(lambda x: x < 5, dataAngka))}")
print(f"Filter Lambda(2) : {list(filter(lambda x: (x % 2 == 0), dataAngka))}\n")

#* Anonymous Function
# curyying <- dari Haskell Curry 
def pangkatN(angka, n):
    return angka**n

print(f"Fungsi Biasa = {pangkatN(4, 2)}")

# Dengan Currying Menjadi:
def pangkatN(n):                            # Fungsi Luar (def)
    return lambda angka: angka**n           # Fungsi Dalam (lambda)

pangkat2 = pangkatN(2)                      # Akan mengembalikan (return) --> lamba angka: angka**2
print(f"pangkat2 = {pangkat2(4)}")          # Jadi yang awal, dia mengembalikan fungsi bagian dalam (lambda)
pangkat3 = pangkatN(3)
print(f"pangkat3 = {pangkat3(4)}")

print(f"pangkat bebas = {pangkatN(4)(5)}")