print("PROGRAM LATIHAN 1 TUGAS MPP")
lt1 = int(input("masukkan luas tanah1 : "))
lt2 = int(input("masukkan luas tanah2 : "))
lb1 = int(input("masukkan luas bangunan1 : "))
lb2 = int(input("masukkan luas bangunan2 : "))
wt = int(input("masukkan waktu tempuh : "))
tarif = int(input("masukkan tarif : "))

sisa_tanah = lt1*lt2-lb1*lb2
waktu_tempuh = sisa_tanah/wt
tarif_bayar = tarif*waktu_tempuh
print("tarif yg harus dibayar : ", tarif_bayar)