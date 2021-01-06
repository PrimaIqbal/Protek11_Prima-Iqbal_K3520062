# Nomor 2
import datetime
while True:
    kode = input("Masukkan Kode Member  = ")
    nama = input("Masukkan Nama Member	= ")
    judul = input("Masukkan Judul Buku   = ")

    print("\n")
    pil = input("Coba ulangi lagi (y/n) = ")
    print("\n")

    if pil == "n":
        s = datetime.date.today()
        batas = datetime.timedelta(days=7)
        pinjam = str(s+ batas)
        data = open("c:/Users/Prima Iqbal/Documents/No 2.txt", "a+")
        data.write(kode + "|" + nama + "|" + judul + "|" + hariini + "|" + pinjam + "\n")
        data.close
        data = open("c:/Users/Prima Iqbal/Documents/No 2.txt", "r")
        print("data yang pinjam :")
        print(data.read())
        data.close()
        break
    elif pil == "y":
        s = datetime.date.today()
        batas = datetime.timedelta(days=7)
        pinjam = str(s+ batas)
        data = open("c:/Users/Prima Iqbal/Documents/No 2.txt", "a+")
        data.write(kode + "|" + nama + "|" + judul + "|" + hariini + "|" + pinjam + "\n")
        data.close
        continue
    else:
        print("input salah")
        exit()
