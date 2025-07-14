def helloWorld(nama):
    print(f"Selamat Datang Dunia {nama}")

helloWorld("Ucup")
helloWorld("Asyep")

def tambah(angka1, angka2):
    print(f"{angka1} + {angka2} = {angka1 + angka2}")

tambah(1, 5)
tambah(1000, 1)

def sayHi(listPeserta):
    dataPeserta = listPeserta.copy()
    for peserta in dataPeserta:
        print(f"Yang Terhormat {peserta}")

anggotaBoyband = ["Ucup", "Otong", "Dudung"]

sayHi(anggotaBoyband)