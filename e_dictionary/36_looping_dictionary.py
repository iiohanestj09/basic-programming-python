temanDict = {
    'cup' : 'ucup surucup',
    'tong' : 'otong surotong',
    'dung' : 'dudung surudung',
    'sep' : 'asep si kasyep',
    'cuy' : 'ucuy surucuy'
}

# Looping First Try (yang keluar adalah key-nya)

for teman in temanDict:
    print(teman)
    
# Operator Untuk Mengambil Item / Iterables
# Keys
print(f"\n{temanDict.keys()}\n")

for key in temanDict.keys():
    print(temanDict.get(key))

# Values
print(f"\n{temanDict.values()}\n")

for value in temanDict.values():
    print(value)

# Items --> keys : values
print(f"\n{temanDict.items()}\n")

for key,value in temanDict.items():
    print(f"key = {key}, value = {value}")