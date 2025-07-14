# Validasi Pin Harus Angka 4 dan 6 Digit, Tidak boleh ada Simbol-Simbol Lain

def check(pin):
    if type(pin) != str or len(pin) not in [4, 6]:
        return False
    
    for i in pin:
        if i not in "0123456789":
            return False
        
    return True

print(check("1234"))
print(check("000099"))
print(check("123"))
print(check("12345"))
print(check("-1234"))
print(check("+5678"))
print(check("12 34"))
print(check("12.34"))
print(check("12a4"))
print(check("1234\n"))

print("=" * 15)

#^ Cara Gampang
def validatePin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

print(validatePin("1234"))
print(validatePin("000099"))
print(validatePin("123"))
print(validatePin("12345"))
print(validatePin("-1234"))
print(validatePin("+5678"))
print(validatePin("12 34"))
print(validatePin("12.34"))
print(validatePin("12a4"))
print(validatePin("1234\n"))
