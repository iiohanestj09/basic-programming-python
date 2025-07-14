dataDict = {
    'cup' : 'ucup surucup',
    'tong' : 'otong surotong',
    'dung' : 'dudung surudung'
}
print(f"{dataDict}\n")

# Panjang Dictionary
LENDICT = len(dataDict)
print(f"Panjang dictionary = {LENDICT}")

# Mengecek Key Exist atau Tidak
KEY = "cup"
CHECKKEY = KEY in dataDict
print(f"Apakah key {KEY} ada di dataDict = {CHECKKEY}")

# Mengakses Value (Read) dengan get
print(dataDict['cup'])
# print(dataDict['hayo'])         Data Yang tidak ada akan eror di terminal
print(dataDict.get('cup'))
print(dataDict.get('hayo'))     # hasilnya akan 'None' karena tidak ada di dict

# Meng-update Data
dataDict['cup'] = "cap cip cup"     # Key yang Exist
dataDict['kim'] = "Kim Jong Un"     # Key yang Tidak Exist akan dibuat baru
print(f"{dataDict}\n")

dataDict.update({"cup" : "ucup Terganteng"})        # Update
dataDict.update({"faqih" : "Faqoh terkweren"})      # Menambahkan
print(f"{dataDict}\n")

# Men-delete data di Dictionary
del dataDict['faqih']
print(dataDict)


