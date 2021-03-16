#Nama   : William Christian
#NIM    : 71200665
#Grup A

'''Dinna merupakan mahasiswa jurusan Informatika, ia ingin membuat program yang dapat menampilkan bentuk
segitiga sama sisi tetapi ia sedikit kesulitan dalam pembuatan programnya bantulah dinna untuk menyelesaikan
programnya.'''

ukuran = int(input("Masukkan ukuran piramida yang ingin dibuat : "))
jarak = ukuran - 1
for i in range(0, ukuran):
    for j in range(0, jarak):
        print(' ', end='')
    jarak -= 1
    for j in range(0, i + 1):
        print('* ', end='')
    print('')
