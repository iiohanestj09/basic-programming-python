# Ngeprint List Tanpa Spasi DAN KOMA

if __name__ == '__main__':
    n = 5
                                          #! range(x,y) --> x, x+1, x+2, ..., y-1
    listX = [i for i in range(1,n+1)]     #! Sehingga membuat list dari 1 sampai 5
    print("".join(map(str, listX)))       #! Map --> Casting Tipe Data Dalam List, udh gitu simpelnya
        