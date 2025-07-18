from . import Operasi

def readConsole():
    dataFile = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"
    
    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(dataFile):
        dataBreak = data.split(",")
        pk = dataBreak[0]
        dateAdd = dataBreak[1]
        penulis = dataBreak[2]
        judul = dataBreak[3]
        tahun = dataBreak[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")
        
    # Footer
    print("="*100+"\n")
    
    
def createConsole():
    print("\n"+"="*100)
    print("Silahkan Tambah Data Buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Tidak Valid")
        except:
            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)!")
    
    Operasi.create(tahun,judul,penulis)
    print("\nBerikut Adalah Data Baru Anda")
    readConsole()
    
def updateConsole():
    readConsole()
    while True:
        print("Silahkan Pilih Nomor Buku Yang Akan Diupdate")
        noBuku = int(input("Nomor Buku: "))
        dataBuku = Operasi.read(index=noBuku)
        
        if dataBuku:
            break
        else:
            print("Nomor Tidak Valid, Silahkan Masukkan Lagi!")
        
    dataBreak = dataBuku.split(',')
    pk = dataBreak[0]
    dateAdd = dataBreak[1]
    penulis = dataBreak[2]
    judul = dataBreak[3]
    tahun = dataBreak[4][:-1]
    
    while True:
        # Data yang Ingin Di-Update
        print("\n"+"="*100)
        print("Data yang Ingin Anda Hapus")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # Memilih Mode untuk update
        userOption = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match userOption:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun Tidak Valid")
                    except:
                        print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)!")
            case _: print("Index tidak Valid")
            
        print("Data Baru Anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        isDone = input("Apakah Anda Yakin (y/n): ")
        if isDone == "y" or isDone == "Y":
            break       
    
    Operasi.update(noBuku,pk,dateAdd,tahun,judul,penulis)     


def deleteConsole():
    readConsole()
    while True:
        print("Silahkan Pilih Nomor Buku Yang Akan Di-delete")
        noBuku = int(input("Nomor Buku: "))
        dataBuku = Operasi.read(index=noBuku)
        
        if dataBuku:
            dataBreak = dataBuku.split(',')
            pk = dataBreak[0]
            dateAdd = dataBreak[1]
            penulis = dataBreak[2]
            judul = dataBreak[3]
            tahun = dataBreak[4][:-1]
            
            
            # Data yang ingin Di-Delete
            print("\n"+"="*100)
            print("Data yang Ingin Anda Hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            isDone = input("Apakah Anda Yakin (y/n): ")
            if isDone == "y" or isDone == "Y":
                Operasi.delete(noBuku)
                break
        else:
            print("Nomor Tidak Valid, Silahkan Masukkan Lagi")
    
    print("Data Berhasil Dihapus")