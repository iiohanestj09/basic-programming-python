import datetime as dt

print("Silahkan Masukkan Tanggal, Bulan Dan Tahun Lahir Anda")
tanggal = int(input(f"{"Tanggal":<10}: "))
bulan = int(input(f"{"Bulan":<10}: "))
tahun = int(input(f"{"Tahun":<10}: "))
tanggalLahir = dt.date(tahun, bulan, tanggal)
tanggalSekarang = dt.date.today()

print(f"Tanggal Lahir Anda = {tanggalLahir}")
print(f"Hari Lahir Anda    = {tanggalLahir:%A}\n")
print(f"Tanggal Hari Ini   = {tanggalSekarang}")
print(f"Hari Ini Adalah    = {tanggalSekarang:%A}\n")

umurHari = tanggalSekarang - tanggalLahir
umur = umurHari.days // 365
bulanSisa = (umurHari.days % 365) // 30
hariSisa = (umurHari.days % 365) % 30
print(f"Maka, Umur Anda Sekarang Adalah {umur} Tahun, {bulanSisa} Bulan, {hariSisa} Hari")
print(f"Selamat, Anda Sudah Bertahan Hidup Selama {umurHari.days} Hari Di Bumi")

