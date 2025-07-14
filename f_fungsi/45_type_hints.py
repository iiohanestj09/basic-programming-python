# type hints --> Mengetahui tipe data parameter dari sebuah fungsi

import string

def bagiSepuluh(paramX:int) -> int:     # :int == inputnya Harusnya INT; -> int == Outputnya Harusnya INT
    return paramX / 10

print(bagiSepuluh(40))
print(bagiSepuluh(25))

def tampil(paramX:string):    #! Harusnya import string
    print(paramX)

tampil("Ucup")

