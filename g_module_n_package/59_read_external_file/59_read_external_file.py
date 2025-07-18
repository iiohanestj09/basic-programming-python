print(f"{"="*3}Membaca File txt{"="*3}")
berkas = open("contohData.txt", mode="r")

print(f"Status read : {berkas.readable()}")
print(f"Status write: {berkas.writable()}\n")

## baca seluruh file
# print(berkas.read())

## baca per baris
print(berkas.readline())            # baca baris pertama + semacam \n di baris pertama
print(berkas.readline(),end="")     # baca baris kedua
print(berkas.readline(),end="")     # baca baris ketiga

## baca semua baris sebagai list
# print(berkas.readlines())         # readlineS

print(f"\n\nApakah File Sudah Di close: {berkas.closed}")    # Otomotas Close File, karena ada di luar WITH
berkas.close()
print(f"Apakah File Sudah Diclose: {berkas.closed}")      # Otomotas Close File, karena ada di luar WITH


## Salah Satu Teknik membuka File di Python
print(f"\n{"="*3}Membaca File txt dengan WITH{"="*3}")

with open("contohData.txt", mode="r") as berkasX:
    konten = berkasX.readline()
    print(konten,end="")
    print(f"\nApakah File Sudah Diclose: {berkasX.closed}")
    
print(f"Apakah File Sudah Diclose: {berkasX.closed}")      # Otomotas Close File, karena ada di luar WITH
