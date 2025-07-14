# INTEGER
dataInt = 9
dataStr = str(dataInt)
dataFloat = float(dataInt)      
dataBool = bool(dataInt)
print("Int   =", dataInt, ", type:", type(dataInt))
print("Str   =", dataStr, ", type:", type(dataStr))
print("Float =", dataFloat, ", type:", type(dataFloat))
print("Bool  =", dataBool, ", type:", type(dataBool), "\n")

# STRING 
dataStr = "0"
dataInt = int(dataStr)
dataFloat = float(dataStr)      
dataBool = bool(int(dataStr))       #! ==> ubah ke INT lalu ke BOOL
print("Str   =", dataStr, ", type:", type(dataStr))
print("Int   =", dataInt, ", type:", type(dataInt))
print("Float =", dataFloat, ", type:", type(dataFloat))
print("Bool  =", dataBool, ", type:", type(dataBool), "\n")

# FLOAT
dataFloat = -7.0
dataInt = int(dataFloat)
dataStr = str(dataFloat)      
dataBool = bool(dataFloat)
print("Float =", dataFloat, ", type:", type(dataFloat))
print("Int   =", dataInt, ", type:", type(dataInt))
print("Str   =", dataStr, ", type:", type(dataStr))
print("Bool  =", dataBool, ", type:", type(dataBool), "\n")

# BOOL
dataBool = True
dataInt = int(dataBool)
dataStr = str(dataBool)      
dataFloat = float(dataBool)
print("Bool =", dataBool, ", type:", type(dataBool))
print("Int   =", dataInt, ", type:", type(dataInt))
print("Str   =", dataStr, ", type:", type(dataStr))
print("Float  =", dataFloat, ", type:", type(dataFloat))