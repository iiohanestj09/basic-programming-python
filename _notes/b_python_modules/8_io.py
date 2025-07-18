# ┌────────────────────────────┬───────────────────────────────────────────────────────────────────────┐
# │         Kelas/Fungsi       │ Deskripsi                                                             │
# ├────────────────────────────┼───────────────────────────────────────────────────────────────────────┤
# │ IOBase                     │ Kelas dasar untuk semua jenis stream I/O                              │
# │ RawIOBase                  │ Kelas I/O mentah (unbuffered), langsung byte                          │
# │ BufferedIOBase             │ Kelas I/O biner buffered untuk efisiensi                              │
# │ TextIOBase                 │ Kelas I/O teks yang menangani encoding dan decoding                   │
# │ FileIO                     │ Akses file secara langsung (raw) dalam mode biner                     │
# │ BufferedReader             │ Membaca stream biner dengan buffering                                 │
# │ BufferedWriter             │ Menulis stream biner dengan buffering                                 │
# │ BufferedRWPair             │ Kombinasi baca/tulis buffered                                         │
# │ BufferedRandom             │ Buffered stream dengan akses acak (seekable)                          │
# │ BytesIO                    │ Stream biner dalam memori (pakai bytes)                               │
# │ StringIO                   │ Stream teks dalam memori (pakai string)                               │
# │ TextIOWrapper              │ Wrapper teks untuk stream biner, tangani encoding                     │
# │ open(filename, mode, ...)  │ Membuka file (mirip built-in `open`, tapi dari `io`)                  │
# │ open_code(filename)        │ Membuka file sebagai kode Python (mode 'rb')                          │
# │ DEFAULT_BUFFER_SIZE        │ Ukuran buffer default (biasanya 8192 byte)                            │
# │ text_encoding(...)         │ Menentukan encoding default teks                                      │
# │ UnsupportedOperation       │ Exception untuk operasi I/O yang tidak didukung                       │
# │ BlockingIOError            │ Exception jika operasi I/O diblokir                                   │
# └────────────────────────────┴───────────────────────────────────────────────────────────────────────┘
