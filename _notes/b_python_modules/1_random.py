# ┌────────────────────────────┬────────────────────────────────────────────────────────────────────────────┐
# │           Method           │ Deskripsi                                                                  │
# ├────────────────────────────┼────────────────────────────────────────────────────────────────────────────┤
# │ seed(x)                    │ Inisialisasi generator angka acak (untuk hasil tetap)                      │
# │ getstate()                 │ Mengambil status internal dari generator angka acak                        │
# │ setstate(state)            │ Mengembalikan status internal generator ke kondisi sebelumnya              │
# │ getrandbits(k)             │ Mengembalikan angka acak sebagai bit (integer) sebanyak k bit              │
# │ randrange(start, stop)     │ Mengembalikan angka acak dalam rentang tertentu                            │
# │ randint(a, b)              │ Mengembalikan angka acak antara a dan b (inklusif)                         │
# │ choice(seq)                │ Mengambil satu elemen acak dari sebuah urutan (list, tuple, dsb)           │
# │ choices(seq, k=1)          │ Mengambil beberapa elemen acak dari urutan (boleh duplikat)                │
# │ shuffle(seq)               │ Mengacak urutan elemen dalam list                                          │
# │ sample(seq, k)             │ Mengambil subset acak dari urutan (tanpa duplikat)                         │
# │ random()                   │ Mengembalikan float acak antara 0 dan 1                                    │
# │ uniform(a, b)              │ Float acak antara dua angka yang diberikan                                 │
# │ triangular(low, high, mode)│ Float acak dengan distribusi segitiga, bisa tentukan titik puncak          │
# │ betavariate(alpha, beta)   │ Float acak dengan distribusi Beta antara 0 dan 1                           │
# │ expovariate(lambd)         │ Float acak dengan distribusi Eksponensial                                  │
# │ gammavariate(alpha, beta)  │ Float acak dengan distribusi Gamma                                         │
# │ gauss(mu, sigma)           │ Float acak dengan distribusi Gaussian/Noramal (mean & deviasi)             │
# │ lognormvariate(mu, sigma)  │ Float acak dengan distribusi log-normal                                    │
# │ normalvariate(mu, sigma)   │ Float acak berdasarkan distribusi normal                                   │
# │ vonmisesvariate(mu, kappa) │ Float acak berdasarkan distribusi Von Mises (statistik arah)               │
# │ paretovariate(alpha)       │ Float acak dengan distribusi Pareto                                        │
# │ weibullvariate(alpha, beta)│ Float acak dengan distribusi Weibull                                       │
# └────────────────────────────┴────────────────────────────────────────────────────────────────────────────┘
