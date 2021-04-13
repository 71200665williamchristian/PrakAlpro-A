#Nama   : William Christian
#NIM    : 71200665
#Grup A

'''Tina memiliki seorang kekasih yang sangat amat posesif, oleh karena itu Tina
berusaha untuk menyimpan password HPnya di dalam file dalam computer agar tidak lupa
sewakt-waktu. Namun jika disimpan dengan file langsung maka password Tina akan ketahuan.
Kamu sebagai programmer akan membantu Mengenerate password tina kedalam decimal perlu
diingat bahwa password harus merupakan bagian dari Hexadecimal!'''


arsip = open('password.txt','w')

password = str(input("Masukkan password yang akan di generate: "))
panjang = len(password) - 1
total = 0
for i in password:
    if i == 'F':
        hitung = 15*(16**panjang)
        total += hitung
        panjang -= 1
    elif i == 'E':
        hitung = 14*(16**panjang)
        total += hitung
        panjang -= 1
    elif i == 'D':
        hitung = 13*(16**panjang)
        total += hitung
        panjang -= 1
    elif i == 'C':
        hitung = 12*(16**panjang)
        total += hitung
        panjang -= 1
    elif i == 'B':
        hitung = 11*(16**panjang)
        total += hitung
        panjang -= 1
    elif i == 'A':
        hitung = 10*(16**panjang)
        total += hitung
        panjang -= 1
    else:
        hitung = int(i)*(16**panjang)
        total += hitung
        panjang -= 1

masukkan = arsip.write(str(total))