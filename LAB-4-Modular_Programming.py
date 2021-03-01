#Nama   : William Christian
#NIM    : 71200665
#Grup A

print("="*5,"Progam Penghitung Volume","="*5)

def volume_balok(panjang,lebar,tinggi):
    jumlah = panjang * lebar * tinggi
    return jumlah
def volume_kubus(sisi):
    total = sisi**3
    return total
def volume_tabung(jari,tinggi):
    hasil = 3.14 * (jari**2) * tinggi
    return hasil
try:
    print("Fungsi penghitungan yang dapat dilakukan :")
    print("1. Volume Balok")
    print("2. Volume Kubus")
    print("3. Volume Tabung")
    pilih = int(input("Masukkan pilihan Anda : "))

    if pilih == 1:
        panjang = float(input("Masukkan panjang : "))
        lebar = float(input("Masukkan lebar : "))
        tinggi = float(input("Masukkan tinggi : "))
        print("Volume Balok adalah",volume_balok(panjang,lebar,tinggi))
    elif pilih == 2:
        sisi = float(input("Masukkan sisi : "))
        print("Volume Kubus adalah",volume_kubus(sisi))
    elif pilih == 3:
        jari = float(input("Masukkan jari-jari : "))
        tinggi = float(input("Masukkan tinggi : "))
        print("Volume Tabung adalah",volume_tabung(jari,tinggi))
    else:
        print("Fungsi yang ingin anda gunakan tidak tersedia.")
