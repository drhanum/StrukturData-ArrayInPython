A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

hasil = [[A[i][j] + B[i][j] 
          for j in range(len(A[0]))] 
            for i in range(len(A))]

for baris in hasil:
    print(baris)