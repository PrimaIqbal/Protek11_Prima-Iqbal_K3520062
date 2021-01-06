#Nomor 3
import datetime
f = open("c:/Users/Prima Iqbal/Documents/No3.txt", "r")
data  = []
data2 = []
data3 = []
data4 = []

for line in f:
    spl = line.split("|")
    data.append(spl[0])
    data2.append(spl[1])
    data3.append(spl[2])
    data4.append(spl[3])

pil = str(input("Masukkan kode member mau cari : "))
if pil in data:
    ketemu = True
    a = data.index(pil)
    NOW = datetime.datetime.now()
    x = data5[a]
    from datetime import datetime
    x = datetime.strptime(x, "%Y-%m-%d")
else:
    print("data tidak ketemu")
    exit()
if ketemu == True:
    r = datetime.date(NOW) - maksimal
    r = int(r.days)
    bayardenda = 0
    if r >= 0:
        bayardenda = 2000 *(r)
        r = abs(r)
    elif r <= 0:
        r = 0

    print("\nData Peminjaman Buku\n"
         "\nKode Member                    : ",data1[a],
         "\nNama Member                    : ",data2[a],
         "\nJudul Buku                     : ",data3[a],
         "\nTanggal Mulai Peminjaman       : ",data4[a],
         "\nTanggal Maks Peminjaman        : ",data5[a],
         "\nTanggal Pengembalian           : ",pengembalian,
         "\ntelat                          : ", r ,"Hari"
         "\nTotal denda                    :  Rp.",bayar)

else:
    print("data tidak ketemu")
