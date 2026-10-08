def kali_matriks(A, B):
    baris_A, kolom_A = len(A), len(A[0])
    baris_B, kolom_B = len(B), len(B[0])

    if kolom_A != baris_B:
        raise ValueError("Jumlah kolom A harus sama dengan jumlah baris B")

    hasil = [[0 for i in range(kolom_B)] 
             for j in range(baris_A)]

    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

for baris in kali_matriks(A, B):
    print(baris)