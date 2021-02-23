#Nama   : William Christian
#NIM    : 71200665
#Grup A

"""Dina mendapatkan tugas matematika untuk menghitung luas bangun datar yaitu persegi, persegi panjang dan segitiga.
bantulah dina agar tugas yang dikerjakannya lebih mudah dan cepat untuk diselesaikan, dengan cara membuat program yang
dapat menghitung luasan bangun datar."""


print("==========PROGRAM PENGHITUNGAN LUAS BANGUN DATAR==========")
print()
nama = str(input("Masukkan Nama : "))
print("Bangun datar yang dapat dihitung :")
print("1. Persegi")
print("2. Persegi panjang")
print("3. Segitiga")
try:
    pilihan = int(input("Masukkan pilihan anda : "))
    if pilihan == 1 :
        sisi = float(input("Masukkan nilai sisi : "))
        hasil_persegi = sisi * sisi
        print("Luas persegi adalah",hasil_persegi)
    elif pilihan == 2 :
        panjang = float(input("Masukkan nilai panjang : "))
        lebar = float(input("Masukkan nilai lebar : "))
        hasil_persegipanjang = panjang * lebar
        print("Luas persegi panjang adalah",hasil_persegipanjang)
    elif pilihan == 3 :
        alas = float(input("Masukkan nilai alas : "))
        tinggi = float(input("Masukkan nilai tinggi : "))
        luas_segitiga = 1/2 * alas * tinggi
        print("Luas segitiga adalah",luas_segitiga)
    else :
        print("Maaf kami hanya menyediakan pilihan diatas")
except:
    print("Maaf yang anda input yang anda masukkan tidak valid")