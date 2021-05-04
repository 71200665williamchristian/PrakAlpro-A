'''Dito ingin melakukan pendataan karyawan kantornya sekaligus menentukkan sesi kerja dari setiap
karyawannya, tetapi bila dilakukan secara konvensional data akan mudah untuk hilang dan jangka waktu
media penyimpanannya tidak panjang. maka dari itu dito bermaksud untuk membuat program yang dapat mendata
dan menampilkan data dalam bentuk tuple tetapi ia tidak paham dalam membuat program. sebagai sahabatnya
bantulah dito untuk membuat program tersebut. '''

hari = ('Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu')
x = 0
karyawan = []
shift = []

try:

    for i in range (len(hari)):
        nama = str(input("Masukkan nama karyawan pada hari %s : " %hari[x]))
        x += 1
        sesi = str(input("Masukkan shift kerja keryawan : "))
        print()
        karyawan.append(nama)
        shift.append(sesi)
    
    print('='*20,"Jadwal Kerja Karyawan",'='*20)
    y = 0 
    for j in range (len(hari)):
        print("Pegawai yang bekerja pada hari %s shift %s adalah %s" %(hari[y],shift[y],karyawan[y]))
        y += 1

except:
    print("Perhatikan kembali input yang anda tambahkan")