# List Comperhensive atau Nested List

# Tugas, membuat List 3D dan menolak isi dari List tersebut memiliki sum 'n'
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    dataList = []

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k != n:          #! Menolak jika sum ijk ini bernilai n
                    dataList.append([i,j,k])
                
    print(dataList)

#& Contoh input: x=1, y=1, z=2, n=3