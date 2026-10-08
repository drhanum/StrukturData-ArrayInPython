# Membuat array 2D menggunakan nested list
arr2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mengakses elemen (baris, kolom)
print("elemen arr2d[0][1]:", arr2d[0][1])
print("elemen arr2d[2][2]:", arr2d[2][2])

# Mengubah elemen
arr2d[1][1] = 50
print("Setelah mengubah elemen di indeks [1][1]:", arr2d[1][1])


# Menelusuri seluruh elemen
for baris in arr2d:
    for elemen in baris:
        print(elemen, end=" ")
    print()


for baris in range(len(arr2d)):
    for kolom in range(len(arr2d[baris])):
        print(arr2d[baris][kolom], end=" ")
    print()

print("while")

i = 0
while i < len(arr2d):
    j = 0
    while j < len(arr2d[i]):
        print(arr2d[i][j], end=" ")
        j += 1
    print()
    i += 1


