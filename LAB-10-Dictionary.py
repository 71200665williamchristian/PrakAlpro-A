'''Dito merupakan seorang pemilik swalayan yang besar di daerahnya, ia mempunyai banyak pegawai tetapi ia merasa kesulitan
dalam mendata pegawainya secara manual. Jadi ia berencana untuk membuat program yang dapat mendata pegawainya tanpa harus 
merepotkannya untuk melakukan pendataan konvensional. Tetapi masalahnya Dito kurang paham dalam hal pembuatan program ini,
Dito berencana untuk meminta bantuanmu dalam membuat program ini karena kamu merupakan temannya yang adalah seorang programmer.
Bantulah Dito untuk membuat program sederhana ini.'''


print("="*15,"Program Pencatat Biodata Pegawai","="*15)
print()
kamus = dict()
kamus_nama = []
kamus_umur = []
value = 0

try:
    banyak = int(input("Berapa banyak biodata pegawai yang ingin anda tambahkan? "))
    print()
    for i in range (banyak):
        nama = str(input("Masukkan nama pegawai: "))
        umur = int(input("Masukkan umur pegawai: "))
        print()

        kamus_nama.append(nama)
        kamus_umur.append(umur)

    for j in range (banyak):
        kamus[kamus_nama[value]] = kamus_umur[value]
        value = value + 1

    print("="*23,"Biodata Pegawai","="*23)
    print(kamus)

    kamus1 = dict()
    urutkan = sorted(kamus.values())
    key = kamus.keys()

    for a in urutkan:
        for b in key:
            if kamus[b] == a:
                kamus1[a] = b

    print()
    print("="*14,"Biodata Pegawai Setelah Diurutkan","="*14)
    print(kamus1)
except:
    print("INVALID INPUT!")