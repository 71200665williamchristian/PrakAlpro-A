'''Tania merupakan mahasiswa informatika ukdw dia adalah seseorang yang senang akan 
bahasa, dan budaya romawi, ia juga sangat senang apabila ada yang membahas tentang angka 
romawi, biasanya hal itu menjadi permaianan di dalam tongkrongannya sembari bercanda mereka
memainkan permainan tebak-tebakan angka romawi ini. untuk mengoreksi apakah jawaban mereka 
benar atau salah tania telah menyiapkan program yang telah ia bangun untuk permainan tebak-
tebakan angka romawi ini agar tahu jawaban dari tebakan mereka'''


import re
romawi = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}

angka = str(input("Masukkan angka = "))

regex = re.findall(r'(?=\b[MDCLXVI]+\b)M{0,20}(?:CM|CD|D?C{0,20})(?:XC|XL|L?X{0,20})(?:IX|IV|V?I{0,20})', angka)

res = []
count = 0
for i in (regex):
    for j in i:
        res.append(j)

for j in res:
    count+=romawi[j]
print(count)