print("Hello World")        #! Keduanya Sama, baik "" dan ''
print('Hello World Juga')

print("Ada Kata 'World'")
print('Kata Putra: "Hello World"\n')

nama = "Putra Dae"
ips1= 3.94

print("Bagian I:")
print("Perkenalkan Nama Saya:", nama)
print("Umur Saya", 19, "Tahun")
print("IPS 1 Saya:", ips1,"\n")

print("Bagian II:")
print("Perkenalkan Nama Saya: " + nama)
print("Umur Saya " + str(19) + " Tahun")       #! Print menggunakan (,), (+), dan f-string
print("IPS 1 Saya: " + str(ips1) + "\n")

print(f"Bagian III:")
print(f"Perkenalkan Nama Saya: {nama}")
print(f"Umur Saya 19 Tahun")
print(f"IPS 1 Saya: {ips1}")

print("""
Bagian IV:
Perkenalkan Nama Saya: Putra Dae
Umur Saya 19 Tahun
IPS 1 Saya: 3.94
""")

#? Cara run code di terminal: " py 'namaFile'.py "
#& FYI: Python juga bisa compile file dulu, biar performanya lebih efisien
#& ketik di terminal: " python -m py_compile 'namaFile'.py " => tersimpan di file '__pycache__'
#& Cara Run File Compile Pyhton "python 'namaFile'.py"
