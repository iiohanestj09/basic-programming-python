# Sebagai pengenalan dengan GUI --> Graphical User Interface

# init
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Varibel dan Fungsi
window = tk.Tk()                                   # Membuat Variabel Window == jendela lain dari terminal
window.configure(bg="white")                       # bg == background, bg windownya warna putih
window.geometry("300x200")                         # geometri -> ukuran windownya
window.resizable(False, False)                     # agar windownya memiliki ukuran yang tetap
window.title("Sapa Dia!")                          # Membuat Judul dari window

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombolClick():                                 # Fungsi ini akan dipanggil di tombol
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteenggggg :)"
    showinfo(title="Whazzup!", message=pesan)      # Akan ditampilkan di JENDELA BARU


# Frame Input
inputFrame = ttk.Frame(window)
# penempatan Grid, Pack, Place
inputFrame.pack(padx=10, pady=10, fill="x", expand=True)

# Komponen-komponen
# 1. Label Nama Depan
namaDepan_label = ttk.Label(inputFrame, text="Nama Depan")
namaDepan_label.pack(padx=10, fill="x", expand=True)
# 2. Entry Nama Depan
namaDepan_entry = ttk.Entry(inputFrame, textvariable=NAMA_DEPAN)
namaDepan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label Nama Belakang
namaBelakang_label = ttk.Label(inputFrame, text="Nama Belakang")
namaBelakang_label.pack(padx=10, fill="x", expand=True)
# 4. Entry Nama Belakang
namaBelakang_entry = ttk.Entry(inputFrame, textvariable=NAMA_BELAKANG)
namaBelakang_entry.pack(padx=10, fill="x", expand=True)

# 5. Tombol
tombolSapa = ttk.Button(inputFrame, text="Sapa!", command=tombolClick)
tombolSapa.pack(padx=10, pady=10, fill="x", expand=True)

# Main Lopp Window
window.mainloop()