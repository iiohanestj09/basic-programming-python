# Copy Dictionary
teman2Dict = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung'
}

friendsDict = teman2Dict.copy()

print(f"teman2Dict: {teman2Dict}")
print(f"friendsDict: {friendsDict}\n")

teman2Dict['cup'] = "ucup si kewren"
print(f"teman2Dict: {teman2Dict}")
print(f"friendsDict: {friendsDict}\n")

# pop Dictionray (Berdasarkan Key)
dataOtong = friendsDict.pop('tong')
print(f"dataOtong: {dataOtong}")
print(f"friendsDict: {friendsDict}\n")

# popitem Dictionary (Yang Terkahir Saja)
dataTerakhir = friendsDict.popitem()
print(f"dataTerakhir: {dataTerakhir}")
print(f"friendsDict: {friendsDict}\n")
