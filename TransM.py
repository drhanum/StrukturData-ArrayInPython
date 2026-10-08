def transpose(matriks):
    baris = len(matriks)
    kolom = len(matriks[0])
    hasil = [[matriks[j][i] for j in range(baris)] for i in range(kolom)]
    return hasil

M = [[1, 2, 3], 
     [4, 5, 6]]

i = 0
while i < len(M[0]):
    j = 0
    while j < len(M):
        print(M[i][j], end=" ")
        j += 1
    print()
    i += 1


for baris in transpose(M):
    print(baris)