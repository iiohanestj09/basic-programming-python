
#* If Inline
nama = input("Nama Kamu Siapa (1): ")
if nama == "maman": print("Kamu Ganteng Abiiezzz Maman")


#* If Indentation
nama = input("Nama Kamu Siapa (2): ")
if nama == "ucup":
    print("Kamu Juga Ganteng Bangetttzz Ucup")
    print("Kamu Orang Terganteng Nomor 2 Setelah Maman")
    print("Udah itu Aja")

    
#* Elif dan Else
nama = input("Nama Kamu Siapa (3): ")
if nama == "mario":
    print("Kamu Juga Ganteng Kok Mario")
elif nama == "maria":
    print("Kamu Cantik Banget Maria")
else:
    print("Ah Gak Tau Gak Kenal")

    
#* If Nested
nama = input("Nama Kamu Siapa (4): ")
if nama == "maman":
    cek1 = input("Apakah Kamu Benar-Benar Maman Yang Kukenal? : ")
    if cek1 == "yoi":
        cek2 = input("Hmmm? Berapa Umurmu sekarang? : ")
        if cek2 == "19":
            print("Benar! Ternyata Kamu benar-benar Maman")
    elif cek1 == "iya":
        print("Kamu Bukan Maman Yang Kukenal")
    else:
        print("Dah lah, kamu bukan Maman")
elif nama == "ucup":
    cek3 = input("Apakah Kamu Benar-Benar Ucup Yang Kukenal? : ")
    if cek3 == "yoiii":
        cek4 = input("Hmmm? Berapa Umurmu sekarang? : ")
        if cek4 == "20":
            print("Benar! Ternyata Kamu benar-benar Ucup")
    elif cek3 == "iya":
        print("Kamu Bukan Ucup Yang Kukenal")
    else:
        print("Dah lah, kamu bukan Ucup")
else:
    print("Auh Ah, Gak Kenal")

print("Akhir Dari Program!")
