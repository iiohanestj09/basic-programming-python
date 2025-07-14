nama = "Putra"
umur = 19
tinggiBadan = 156.6
beratBadan = 50.4
fakultas = "Teknik"
hobi = "Coding"

#* Print Manual
print("=======MANUAL=======")
print(f"Nama: {nama}, \nUmur: {umur}, \nTinggi Badan: {tinggiBadan}, \nBerat Badan: {beratBadan}")
print(f"Fakultas: {fakultas}, \nHobi: {hobi}")

#* Print Modifikasi
print(f"""
{"MODIF".center(21,"=")}
{"Nama":<13}: {nama:>7}
{"Umur":<13}: {umur:>7}
{"Tinggi Badan":<13}: {tinggiBadan:>7}
{"Berat Badan":<13}: {beratBadan:>7}
{"Fakultas":<13}: {fakultas:>7}
{"Hobi":<13}: {hobi:>7}
""")
