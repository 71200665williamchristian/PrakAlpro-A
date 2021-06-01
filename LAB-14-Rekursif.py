'''Dito Merupakan murid yang senang berhitung apalagi bila tentang materi rekursif 
pada suatu hari ia ingin membuat program yang dapat menghitung bentuk rekursif 
tetapi karena dito memiliki teman yang juga seorang programmer dia tidak ambil pusing
dan meminta bantuan temannya untuk membuatkannya sebuah program kalkulator rekursif
sebagai teman dito yang baik bantulah ia untuk membuat program tersebut'''

def rekursif(x1, xn):
    for i in range (xn):
        if xn == x1:
            return x1
        else:
            return 2 * rekursif(x1,xn-1) + 1
        
print("==========Kalkulator Rekursif==========")
print()
try:
    x1 = int(input("Masukkan nilai X1 : "))
    xn = int(input("Masukkan n yang dicari : "))
    print("Hasil x%d = " %(xn),end="")
    print(rekursif(x1,xn))
except:
    print("Maaf yang anda inputkan tidak valid")