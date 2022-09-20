print("APLIKASI KASIR MENGGUNAKAN PYTHON")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

total1=0
jenis1=""
porsi=0
gelas=0

def fungsimakanan():
   global total1
   global porsi
   global jenis1
   print ("\n~~~~Menu Makanan~~~~")
   print("1. nasi sayap - Rp15000")
   print("2. nasi paha bawah - Rp9000")
   print("3. nasi dada - Rp11000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       total1=porsi*15000
       print (porsi," nasi + sayap = Rp", total1)
       jenis1=("Nasi sayap")
   elif nomor==2:
       total1=porsi*9000
       print (porsi," nasi + paha bawah = Rp", total1)
       jenis1=("nasi paha bawaah")
   elif nomor==3:
       total1=porsi*11000
       print (porsi, " nasi + dada = Rp", total1)
       jenis1=("nasi dada")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()


fungsimakanan()

total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("\n~~~~Menu Minuman~~~~")
   print("1. Es teh - Rp2000")
   print("2. Es jeruk - Rp3500")
   print("3. Es kopi - Rp4000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       total2=gelas*2000
       print (gelas," Es Teh = Rp", total2)
       jenis2=(" Gelas Es Teh")
   elif nomor==2:
       total2=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", total2)
       jenis2=("Es Jeruk")
   elif nomor==3:
       total2=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", total2)
       jenis2=("Es Kopi")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()


fungsiminuman()
    
totalsemua=0
totalsemua=total1+total2
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("===================================")
data_pembeli = [pembeli, totalsemua, uang]
print(data_pembeli)
print("===================================")

print("\n===================================")
print("======= S T R U K   B E L I =========")
print("======================================")
print (" Nama         :",pembeli)
print (" Beli         :",porsi,jenis1,"-", total1)
print ("               ",gelas,jenis2,"-", total2)
print (" Tagihan      : Rp.",totalsemua)
print (" Uang         : Rp.",uang)
print (" Kembalian    : Rp.",kembalian)
print("========TERIMA KASIH ATAS KUNJUNGAN ANDA============")
print("==========[KONTAK : 0895378979888]=================")