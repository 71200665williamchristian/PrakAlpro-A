''' Doni merupakan orang yang senang untuk bermain dengan data, ia sering bermain dengan data
yang berupa integer maupun data yang berbentuk string. Ia sering menggabungkan dua data kemudian
melakukan pencarian data yang berbeda serta mencari data yang sama. Kemudian Doni berpikiran ingin
membuat program yang dapat melakukan hobby nya itu namun Doni bukanlah seorang programmer yang mahir
sehingga ia berniat untuk meminta bantuanmu dalam membuat program tersebut. '''


isi1 = set()
isi2 = set()

try:
    print("Pilihan bentuk data:")
    print("1. Bentuk data integer")
    print("2. Bentuk data string")
    user1 = int(input("Masukkan bentuk data pilihan anda: "))
    print()

    if user1 == 1:
        banyak_data1 = int(input("Berapa kali ingin memasukkan data pertama? "))
        banyak_data2 = int(input("Berapa kali ingin memasukkan data kedua? "))
        print()

        for i in range (banyak_data1):
            input1 = int(input("Masukkan data pertama: "))
            isi1.add(input1)
        print()
        for j in range (banyak_data2):
            input2 = int(input("Masukkan data kedua: "))
            isi2.add(input2)
        print("="*50)
        print()

    else:
        banyak_data1 = int(input("Berapa kali ingin memasukkan data pertama? "))
        banyak_data2 = int(input("Berapa kali ingin memasukkan data kedua? "))
        print()

        for i in range (banyak_data1):
            input1 = str(input("Masukkan data pertama: "))
            isi1.add(input1)
        print()
        for j in range (banyak_data2):
            input2 = str(input("Masukkan data kedua: "))
            isi2.add(input2)
        print("="*50)
        print()
    
    while True:
        print("Daftar Operasi")
        print("1. Menggabungkan data")
        print("2. Mencari data yang berbeda")
        print("3. Mencari data yang sama")
        print("4. Exit")
        print()

        user2 = int(input("Masukkan operasi yang ingin anda gunakan: "))
        print()

        if user2 == 1:
            print("Isi dari data pertama adalah",isi1)
            print("Isi dari data kedua adalah",isi2)
            print("="*20,"Penggabungan Data","="*20)
            print(isi1.union(isi2))
            print("="*50)
            print()

        elif user2 == 2:
            print("Isi dari data pertama adalah",isi1)
            print("Isi dari data kedua adalah",isi2)
            print("="*20,"Data Berbeda","="*20)
            print(isi1.symmetric_difference(isi2))
            print("="*50)
            print()

        elif user2 == 3:
            print("Isi dari data pertama adalah",isi1)
            print("Isi dari data kedua adalah",isi2)
            print("="*20,"Data Sama","="*20)
            print(isi1.intersection(isi2))
            print("="*50)
            print()
        
        else:
            print("="*18,"Terima Kasih","="*18)
            break

except:
    print("Periksa kembali input yang anda tambahkan")