'''Rio mendapat tugas dari gurunya untuk membuat program yang dapat menyimpan data
dalam bentuk list. tetapi rio sedikit kesulitan dalam membuatnya dan ia ingin meminta
bantuanmu sebagai temannya daari jurusan informatika, dalam pembuatan program penyimpanan
data list ini. bantulah rio untuk membuat program tersebut. '''

print("="*10,"Program Penyimpan Data List","="*10)
print()

penyimpanan = []
try:
    data = int(input("Masukkan data list yang ingin disimpan : "))
    penyimpanan.append(data)

    while True:
        user = str(input("apakah masih ingin menambahkan (ya/tidak)? "))
        if (user == 'ya'):
            data = int(input("Masukkan data list yang ingin disimpan : "))
            penyimpanan.append(data)
        elif (user == 'tidak'):
            penyimpanan.sort()
            print("Data yang anda simpan adalah",penyimpanan)
            print("="*8,"Terima Kasih","="*8)
            break
        else:
            print("Invalid!")
            break
except:
    print("Maaf input anda invalid!")