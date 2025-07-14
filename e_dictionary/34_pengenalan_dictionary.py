# List --> Array
# Menggunakan Index => 0, 1, 2 ...

dataList = ["ucup", "otong", "dadang"]
print(f"{dataList[0]}\n")

# Dictionary --> Associative Array
# Menggunakan Identifier => key

dataDict = {
    "key1" : "value1",
    "key2" : "value2",
    "cp" : "Ucup",
    "tg" : "Otong",
    "dg" : "Dadang",
    "nmbr" : 100,
    "list" : dataList
}

print(f"{dataDict}\n")
print(dataDict['cp'])
print(dataDict['list'])
print(dataDict['nmbr'])

