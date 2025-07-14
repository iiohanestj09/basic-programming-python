from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "XXXXXX",
    "dateAdd": "yyyy-mm-dd",
    "judul": " "*255,
    "penulis": " "*255,
    "tahun": "yyyy"
}

def initConsole():
    try:
        with open(DB_NAME,'r') as berkas:
            print("Database Tersedia, init Done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.createFirstData()