#Nama  : William Christian
#NIM   : 71200665
#Grup A

print("==========PROGRAM PENGHITUNG GAJI KARYAWAN==========")
print("")
nama = str(input("Masukkan Nama Karyawan     : "))
lama = int(input("Berapa Lama Telah Bekerja  : "))
gaji = int(input("Berapa gaji pokok Karyawan : Rp "))
print("")
print("1-3 Tahun mendapat kenaikan sebesar Rp 500000")
print("4-6 Tahun mendapat kenaikan sebesar Rp 1300000")
print("7-10 Tahun mendapat kenaikan sebesar Rp 1700000")
print("")
if (lama >= 1) and (lama <=3) :
    total1 = gaji + 500000
    print("Total gaji",nama,"berjumlah Rp",total1)
elif (lama >= 4) and (lama <= 6) :
    total2 = gaji + 1300000
    print("Total gaji",nama,"berjumlah Rp",total2)
elif (lama >= 7)  and (lama <= 10) :
    total3 = gaji + 1700000
    print("Total gaji",nama,"berjumlah Rp",total3)
else :
    print("Error!")
print("")
print("=============Terima Kasih=============")