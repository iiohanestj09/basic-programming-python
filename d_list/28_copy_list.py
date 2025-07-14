# Teknik Menduplikat di Python
a = 6
b = a       

print(f"a = {a}\nb = {b}")
print(f"a = {hex(id(a))}\nb = {hex(id(b))}\n")  #! Walaupun Addres sama, tapi tidak Terikat

a = 8
print(f"a = {a}\nb = {b}\n{"-"*40}")

x = ["Ucup", "Otong", "Dudung"]
y = x   

print(f"x = {x}\ny = {y}")
print(f"x = {hex(id(x))}\ny = {hex(id(y))}\n")  #! Akan TERIKAT

x[1] = "Michael"    #! => Akan Merubah List 'y' Juga
print(f"x[1] = 'Michael'\nx = {x}\ny = {y}\n")

y.reverse()         #! => Akan Merubah List 'x' Juga
print(f"y.reverse()\nx = {x}\ny = {y}\n{"-"*40}")

#? Cara Yang BENAR ==> .copy()

j = ["Ucup", "Otong", "Dudung"]
k = j.copy()

print(f"j = {j}\nk = {k}")
print(f"j = {hex(id(j))}\nk = {hex(id(k))}\n")  #! TIDAK TERIKAT

k.append("Asep")
print(f'k.append("Asep")\nj = {j}\nk = {k}')


