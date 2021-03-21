#Nama   : William Christian
#NIM    : 71200665
#Grup A

'''Ricky merupakan seorang pelajar yang senang bermain dengan kata dan kalimat. Suatu ketika ia hendak membuat program yang dapat
melakukan beberapa hal terhadap kata dan kalimat seperti menghitung jumlah karakter, mengubah kalimat dengan huruf kercil menjadi 
huruf besar, mengubah kalimat dengan huruf besar menjadi huruf kecil dan memotong kalimat atau kata. bantulah Ricky untuk membuat 
program tersebut.'''

print(8*"=","Program Permainan Kalimat",8*"=")
print()
print("Pilih 1 untuk menghitung banyak karakter")
print("Pilih 2 untuk mengubah kalimat menjadi huruf kecil")
print("Pilih 3 untuk mengubah kalimat menjadi huruf besar")
print("Pilih 4 untuk memotong kata/kalimat")
pilih = str(input("Masukkan pilihan: "))
user = str(input("Masukkan kalimat: "))
try:
    if pilih == str(1):
        hasil = len(user)
        print(hasil)
    elif pilih == str(2):
        hasil1 = user.lower()
        print(hasil1)
    elif pilih == str(3):
        hasil2 = user.upper()
        print(hasil2)
    else:
        startloc = int(input("Start Location: "))
        endloc = int(input("End Location: "))
        hasil3 = user[startloc:endloc]
        print(hasil3)
except:
    print("Maaf, yang Anda masukkan salah silahkan untuk mengulangi program")