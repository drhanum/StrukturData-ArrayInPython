baris, kolom = 3, 4

# Membuat array 2D menggunakan list comprehension
arr2d = [[i+j for j in range(kolom)] for i in range(baris)]

print("Array 2D awal:")
for row in arr2d:
    print(row)