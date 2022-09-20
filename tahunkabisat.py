print("tugas mpp2")
tahun = int(input("tahun : "))

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print ("tahun kabisat")
        else:
            print("bukan tahun kabisat")
    else:
        print("tahun kabisat")
else:
    print("bukan tahun kabisat")