# 1. Mode Write

# Dia akan membuat file baru jika tidak ada,
# lalu akan OVERWRITE isinya

with open("data_1.txt",'w',encoding="utf-8") as berkas:
    berkas.write("jhon si jhonny\n")
    berkas.write("coba\n")

with open("data_1.txt",'w',encoding="utf-8") as berkas:
    berkas.write("ucup sirucup\n")

with open("data_1.txt",'w',encoding="utf-8") as berkas:
    berkas.write("OVERWRITE\n")
    
# 2. Mode Append

with open("data_2.txt",'w',encoding="utf-8") as berkas:
    berkas.write("jhon si jhonny\n")

with open("data_2.txt",'a',encoding="utf-8") as berkas:
    berkas.write("ucup sirucup\n")

with open("data_2.txt",'a',encoding="utf-8") as berkas:
    berkas.write("TAMBAH LAGI KE APPEND")
    
# 3. Mode r+

with open("data_3.txt",'w',encoding="utf-8") as berkas:
    berkas.write("Data ke-3\n")

with open("data_3.txt",'r+',encoding="utf-8") as berkas:
    berkas.write("Baris ke-1\n")
    berkas.write("Baris ke-2\n")
    berkas.write("Baris ke-3\n")

with open("data_3.txt",'r+',encoding="utf-8") as berkas:
    data = berkas.read()
    print(data)

with open("data_3.txt",'r+',encoding="utf-8") as berkas:
    berkas.write("Otong")                   #! MENIMPA isi Text Sesuai dengan Panjang Kalimat