def cetak_matriks(matriks):
    for row in matriks:
        print(row)
 
def pjg_matriks(matriks):
    return len(matriks[0])
 
def lbr_matriks(matriks):
    return len(matriks)
 
def kurangi_matriks(mat_a, mat_b):
    temp_row = []
    temp_mat = []
 
    for i in range(0, lbr_matriks(mat_a)):
        for j in range(0, pjg_matriks(mat_a)):
            temp_row.append(mat_a[i][j] - mat_b[i][j])
        temp_mat.append(temp_row)
        temp_row = []
    return temp_mat
 
matriks_a = [[1, 2, 3, 5], [1, 2, 3, 5], [1, 2, 3, 5]]
matriks_b = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
 
print("matriks_a : ")
cetak_matriks(matriks_a)
 
print("\nmatriks_b : ")
cetak_matriks(matriks_b)
 
print("\nhasil pengurangan : ")
hasil = kurangi_matriks(matriks_a, matriks_b)
cetak_matriks(hasil)
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
