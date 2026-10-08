# Membuat array 1D menggunakan list
arr = [10, 20, 30, 40, 50]

# Mengakses elemen
print("elemen arr[0]:", arr[0])
print("elemen arr[-1]:", arr[-1])

# Mengubah elemen
arr[2] = 99
print("Setelah mengubah elemen di indeks 2:", arr)

# Menambah elemen
arr.append(60)
print("Setelah menambah elemen:", arr)

arr.insert(1, 15)
print("Setelah menyisipkan elemen di indeks 1:", arr)

# Menghapus elemen
arr.pop()
print("Setelah menghapus elemen terakhir:", arr)

arr.remove(99)
print("Setelah menghapus elemen dengan nilai 99:", arr)

# Iterasi
idx = 0
for i in arr:
    print(f"Indeks {idx}: {i}")
    idx += 1


