# Operasi dan Manipulasi String (PART1)

#* 1. Menyambung String (Concatenate)
namaDepan = "Maman"
namaTengah = "D"
namaAkhir = "Luffy"

namaLengkap = namaDepan + " " + namaTengah + "'" + namaAkhir
print("Nama Lengkap: " + namaLengkap + "\n")

#* 2. Menghitung Panjang String {len()}
panjang  = len(namaDepan)
print("Panjang Dari " + namaDepan + " = " + str(panjang))
print("Panjang Dari " + namaLengkap + " = " + str(len(namaLengkap)) + "\n")

#* 3. Operator String
#* 3.1 Mengecek apakah ada char/string di sebuah String {in, not in}
cekD = "D"
status1 = cekD in namaLengkap
print("'D' Ada Di " + namaLengkap + " = " + str(status1))

cekuffy = "uffy"
status2 = cekuffy in namaLengkap
print('"uffy" Ada Di ' + namaLengkap + " = " + str(status2))

status3 = "d" not in namaLengkap
print("'d' Tidak Ada Di " + namaLengkap + " = " + str(status3) + "\n")

#* 3.2 Mengulang String
print("wk" * 7)
print(4 * "keren")
print("-" * 15  + "\n")

#* 3.3 Indexing
print("Index ke-0: " + namaLengkap[0])
print("Index ke-3: " + namaLengkap[3])
print("Index ke-6: " + namaLengkap[6])
print("Index ke-(-1): " + namaLengkap[-1])
print("Index ke-(-2): " + namaLengkap[-2])
print("Index ke-[0:4]: " + namaLengkap[0:5])
print("Index ke-[3:8]: " + namaLengkap[3:9])
print("Index ke-[0,2,4,6,8,10]: " + namaLengkap[0:11:2]  + "\n")

#* 3.4 Item Paling Kecil dan Paling Besar {min, max}
print("Paling Kecil = " + min(namaLengkap))
print("Paling Besar = " + max(namaLengkap))

cobaAscii = ord(" ")
print("ASCII code untuk spasi = " + str(cobaAscii))
cobaData = 117
print("Char untuk ASCII 117 = " + chr(cobaData))
