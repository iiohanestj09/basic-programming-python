import sainsPackage.matematika as mtk       
from sainsPackage import fisika as physics    

print(f"Hasil tambah dari package = {mtk.tambah(1,2,3)}")
print(f"Hasil gaya dari package   = {physics.gaya(9,10)}j")

# terdapat file __pycache__ yang artinya file itu terdapat code python yang sudah di-exe (.pyc)
# kegunaannya agar import-an yang ada disitu tidak di eksekusi ulang, tapi sudah tersimpan di pycache
# dari segi performa juga, file yang sudah di-exe di pycache dapat lebih cepat run programnya
