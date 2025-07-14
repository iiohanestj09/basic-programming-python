# import --> Fungsinya untuk mengambil program dari file ekstrenal .py

# 1. Untuk menyambung program dari eksternal
import program_print
import program_ucup

# 2. Import dengan data
import data_asep
import data_dadang as dadang

    # data ada di namespace module itu
print(data_asep.data)
print(dadang.data)

# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(4, 5)
print(hasil)