import datetime as dt

mahasiswa1 = {
    'nama':'Ucup Surucup',
    'nim':'19022001',
    'sksLulus': 130,
    'beasiswa':False,
    'lahir':dt.datetime(2004,4,10)
}

mahasiswa2 = {
    'nama':'Otong Surotong',
    'nim':'19022002',
    'sksLulus': 140,
    'beasiswa':True,
    'lahir':dt.datetime(2002,10,10)
}

mahasiswa3 = {
    'nama':'Asep Si Kasyep',
    'nim':'19022003',
    'sksLulus': 100,
    'beasiswa':False,
    'lahir':dt.datetime(2000,2,28)
}

dataMahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(f"{'KEY':<8} {'Nama':<17} {'SKS':<4} {'Beasiswa':<10} {'Lahir':<10}")
print("-"*50)

for mahasiswa in dataMahasiswa:
    KEY = mahasiswa
    
    NAMA = dataMahasiswa[KEY]['nama']
    NIM = dataMahasiswa[KEY]['nim']
    SKS = dataMahasiswa[KEY]['sksLulus']
    BEASISWA = dataMahasiswa[KEY]['beasiswa']
    LAHIR = dataMahasiswa[KEY]['lahir'].strftime("%x")
    
    print(f"{KEY:<8} {NAMA:<17} {SKS:<4} {BEASISWA:^10} {LAHIR:<10}")
