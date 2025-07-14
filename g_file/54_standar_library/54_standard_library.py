# Ada Banyak Standard Library Yang ada di Python, bisa dicari di google

import datetime as dt

dataWaktu = dt.datetime.now()
print(f"Data Waktu Sekarang: {dataWaktu}")
print(f"Tahun : {dataWaktu.year}")
print(f"Bulan : {dataWaktu.month}")
print(f"Hari : {dataWaktu.strftime('%A')}")    

from collections import Counter
data = ['a', 'b', 'c', 'a', 'b', 'a', 'd', 'd']
dataCount = Counter(data)

print(f"Data Count: {dataCount}")
print(f"Data Count a: {dataCount['a']}")
print(f"Data Count d: {dataCount['d']}")

import io
file = io.open("file.txt", "r")
print(file.read())

file.close()