#Nama   : William Christian
#NIM    : 71200665
#Grup A

'''Dian merupakan seorang wirausahawan muda. Ia memiliki toko perkakas yang cukup besar di daerahnya, 
dimana toko tersebut tidak pernah sepi pembeli. Setiap hari Dian selalu mendapat keuntungan yang cukup
besar tetapi ia mengalami kesulitan dalam menghitung keuntungan yang ia terima. Maka dari itu bantulah
Dian untuk menghitung keuntungan yang ia dapatkan dengan membuat program penghitung keuntungan.'''

print("="*8,"Program Penghitung Keuntungan","="*8)
print("Rule yang berlaku di dalam program ini:")
print("1. Bila penghitungan Anda masih berlanjut silahkan inputkan 'lanjut'.")
print("2. Bila penghitungan Anda telah selesai silahkan inputkan 'stop'.")

masukkan_user = 'lanjut'
total = 0
try:
    while(masukkan_user == 'lanjut'):
        income = int(input("Masukkan keuntungan yang Anda dapatkan: "))
        total = total + income
        print("Keuntungan yang Anda dapatkan adalah",income)
        masukkan_user = str(input("lanjut/stop? "))
        print()
    else:
        print("Keuntungan keseluruhan yang Anda terima adalah sebesar Rp",total)
        print("="*5,"Terima Kasih","="*5)
except:
    print("Maaf yang Anda inputkan tidak valid")