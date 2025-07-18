import os
import CRUD

if __name__ == "__main__":
    sistemOperasi = os.name
    
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("="*25)
    
    # Check Database itu ada atau tidak
    CRUD.initConsole()
    
    while True:
        os.system("cls")
    
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("="*25)
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data\n")
        
        userOption = input("Masukkan Opsi: ")
        
        match userOption:
            case "1": CRUD.readConsole()
            case "2": CRUD.createConsole()
            case "3": CRUD.updateConsole()
            case "4": CRUD.deleteConsole()
                    
        isDone = input("Ingin Melanjutkan (y/n): ")
        if isDone == "n" or isDone == "N":
            break
        
    print("Program Berakhir, Terima Kasih ^-^")
        