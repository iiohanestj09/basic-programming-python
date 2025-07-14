import datetime as dt
import os
import string
import random

# Template Dictionary Mahasiswa
mahasiswaTemplate = {
    'nama':'nama',
    'nim':'00000000',
    'sksLulus':0,
    'lahir':dt.datetime(1111,1,11)
}

dataMahasiswa = {}
while True:
    os.system("cls")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswaTemplate.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sksLulus'] = input("SKS Lulus: ")
    TANGGALLAHIR = int(input("Tanggal Lahir (1-31): "))
    BULANLAHIR = int(input("Bulan Lahir (1-12):"))
    TAHUNLAHIR = int(input("Tahun lahir (YYYY): "))
    mahasiswa['lahir'] = dt.datetime(TAHUNLAHIR, BULANLAHIR, TANGGALLAHIR)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(4)))
    dataMahasiswa.update({KEY:mahasiswa})         #! meng-Update dari mahasiswa --> database dataMahasiswa
    
    print(f"{'KEY':<8} {'Nama':<17} {'SKS':<4} {'Lahir':<10}")
    print("-"*40)

    for mahasiswa in dataMahasiswa:
        KEY = mahasiswa
        
        NAMA = dataMahasiswa[KEY]['nama']
        NIM = dataMahasiswa[KEY]['nim']
        SKS = dataMahasiswa[KEY]['sksLulus']
        LAHIR = dataMahasiswa[KEY]['lahir'].strftime("%x")
        
        print(f"{KEY:<8} {NAMA:<17} {SKS:<4} {LAHIR:<10}")
    
    print("\n")
    isDone = input("Ingin Menambah Lagi? (y/n): ")
    if isDone == "n":
        break


