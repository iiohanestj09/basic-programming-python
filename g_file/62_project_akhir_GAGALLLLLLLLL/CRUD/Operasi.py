from . import Database
from .Util import randomString
import time
import os

def createFirstData():
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Tidak Valid!")
        except:
            print("Tahun Harus Angka, Silahkan masukkan tahun lagi (yyyy)!")

    data = Database.TEMPLATE.copy()
    
    data['pk'] = randomString(6)
    data['dateAdd'] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)
    
    dataStr = f"{data['pk']},{data['dateAdd']},{data['penulis']},{data['judul']},{data['tahun']}\n" 
    print(dataStr)
    try:
        with open(Database.DB_NAME,'w', encoding="utf-8") as berkas:
            berkas.write(dataStr)
    except:
        print("Gagal Menulis Berkas")
    
        
def read(**kwargs):
    try:
        with open(Database.DB_NAME,'r') as berkas:
            konten = berkas.readlines()
            jumlahBuku = len(konten)
            
            if "index" in kwargs:
                indexBuku = kwargs["index"] - 1
                if indexBuku < 0 or indexBuku > jumlahBuku:
                    return False
                else:
                    return konten[indexBuku]
            else:
                return konten
    except:
        print("Gagal Membaca Database, Error")
        return False
    

def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()
    
    data['pk'] = randomString(6)
    data['dateAdd'] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)
    
    dataStr = f"{data['pk']},{data['dateAdd']},{data['penulis']},{data['judul']},{data['tahun']}\n" 

    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as berkas:
            berkas.write(dataStr)
    except:
        print("Data Gagal Ditambahkan, Error!")
    

def update(noBuku,pk,dateAdd,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()
    
    data['pk'] = pk
    data['dateAdd'] = dateAdd
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)
    
    dataStr = f"{data['pk']},{data['dateAdd']},{data['penulis']},{data['judul']},{data['tahun']}\n" 

    panjangData = len(dataStr)
    
    try:
        with open(Database.DB_NAME,'r+',encoding="utf-8") as berkas:
            berkas.seek(panjangData*(noBuku-1))
            berkas.write(dataStr)
    except:
        print("Gagal Update Data, Error!")

def delete(noBuku):
    try:
        with open(Database.DB_NAME,'r') as berkas:
            count = 0
            
            while True:
                konten = berkas.readline()
                if len(konten) == 0:
                    break
                elif count == noBuku - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as tempBerkas:
                        tempBerkas.write(konten)
                count += 1
    except:
        print("Database Error")
    
    os.rename("data_temp.txt",Database.DB_NAME)