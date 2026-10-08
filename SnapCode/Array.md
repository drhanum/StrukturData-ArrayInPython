# Materi Presentasi: Array dalam Python
### Mata Kuliah Struktur Data

---

## 1. Konsep Dasar Array

### 1.1 Pengertian
Array adalah struktur data yang menyimpan **kumpulan elemen dengan tipe data sejenis**, yang disimpan secara **berurutan (contiguous)** di memori, dan dapat diakses menggunakan **indeks**.

Karakteristik utama array:
- **Ukuran tetap** (pada array "murni"), berbeda dengan list dinamis.
- **Akses acak (random access)** — elemen dapat diakses langsung lewat indeks tanpa harus melewati elemen lain, dengan kompleksitas O(1).
- **Homogen** — seluruh elemen memiliki tipe data yang sama, sehingga alokasi memorinya efisien dan seragam.
- Indeks dimulai dari **0** (zero-based indexing), sama seperti pada kebanyakan bahasa pemrograman termasuk Python.

### 1.2 Array vs List di Python
Ini poin penting yang sering ditanyakan dosen: **Python tidak punya array primitif "asli" seperti C/Java** secara default. Ada tiga cara merepresentasikan array di Python:

| Struktur | Tipe elemen | Ukuran | Sumber |
|---|---|---|---|
| `list` | Heterogen (bisa campur tipe) | Dinamis | Built-in Python |
| `array.array` | Homogen (harus 1 tipe, misal semua `int`) | Dinamis tapi lebih hemat memori | Modul `array` (built-in) |
| `numpy.ndarray` | Homogen, mendukung multidimensi native | Tetap/dinamis, sangat efisien | Library `numpy` (eksternal) |

Untuk presentasi, biasanya cukup fokus ke **`list`** (karena paling umum dipakai) dan menyinggung `array` / `numpy` sebagai pembanding konsep "array asli".

```python
import array

# List: bisa campur tipe data
list_contoh = [1, "dua", 3.0, True]

# array.array: harus 1 tipe data (misal 'i' = integer)
array_contoh = array.array('i', [1, 2, 3, 4])

print(list_contoh)
print(array_contoh)
```

### 1.3 Mengapa Array Penting?
Array menjadi fondasi banyak struktur data lain seperti stack, queue, hash table, dan matriks. Memahami array berarti memahami dasar bagaimana data disusun di memori secara efisien.

---

## 2. Array 1 Dimensi (1D)

### 2.1 Konsep
Array 1D adalah array paling sederhana — berupa **barisan elemen linear** yang diakses dengan satu indeks.

Ilustrasi memori:
```
Indeks :   0    1    2    3    4
Nilai  :  [10, 20, 30, 40, 50]
```

### 2.2 Implementasi di Python

```python
# Membuat array 1D menggunakan list
arr = [10, 20, 30, 40, 50]

# Mengakses elemen
print(arr[0])      # Output: 10
print(arr[-1])     # Output: 50 (indeks negatif = dari belakang)

# Mengubah elemen
arr[2] = 99
print(arr)         # [10, 20, 99, 40, 50]

# Menambah elemen
arr.append(60)      # tambah di akhir
arr.insert(1, 15)   # sisipkan di indeks 1

# Menghapus elemen
arr.pop()            # hapus elemen terakhir
arr.remove(99)       # hapus berdasarkan nilai

# Iterasi
for i in range(len(arr)):
    print(f"Indeks {i}: {arr[i]}")
```

### 2.3 Operasi Umum pada Array 1D
- **Traversal**: mengunjungi seluruh elemen satu per satu.
- **Insertion**: menambahkan elemen baru pada posisi tertentu.
- **Deletion**: menghapus elemen dari posisi tertentu.
- **Searching**: mencari apakah suatu nilai ada dalam array (linear search / binary search).
- **Sorting**: mengurutkan elemen array.

---

## 3. Array 2 Dimensi (2D)

### 3.1 Konsep
Array 2D adalah **array di dalam array** — bisa dibayangkan sebagai tabel dengan **baris (row)** dan **kolom (column)**. Elemen diakses menggunakan dua indeks: `arr[baris][kolom]`.

Ilustrasi:
```
        Kolom 0  Kolom 1  Kolom 2
Baris 0   [1        2        3]
Baris 1   [4        5        6]
Baris 2   [7        8        9]
```

### 3.2 Implementasi di Python

```python
# Membuat array 2D menggunakan nested list
arr2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mengakses elemen (baris, kolom)
print(arr2d[0][1])   # Output: 2 (baris ke-0, kolom ke-1)
print(arr2d[2][2])   # Output: 9

# Mengubah elemen
arr2d[1][1] = 50

# Menelusuri seluruh elemen
for baris in arr2d:
    for elemen in baris:
        print(elemen, end=" ")
    print()
```

### 3.3 Cara Membuat Array 2D dengan Ukuran Tertentu

```python
baris, kolom = 3, 4

# CARA YANG BENAR
arr2d = [[0 for _ in range(kolom)] for _ in range(baris)]

# CARA YANG SALAH (jebakan umum!)
# arr2d_salah = [[0] * kolom] * baris
# Masalahnya: semua baris menunjuk ke objek list yang SAMA di memori.
# Jika satu baris diubah, semua baris ikut berubah!
```

Ini adalah salah satu **jebakan klasik** yang bagus untuk dijelaskan saat presentasi karena menyangkut konsep *reference* di Python.

---

## 4. Matriks

### 4.1 Konsep
Matriks pada dasarnya adalah **array 2D yang direpresentasikan secara matematis**, biasa digunakan untuk operasi aljabar linear (penjumlahan, perkalian matriks, transpose, dsb).

### 4.2 Operasi Matriks Manual (tanpa library)

**a. Penjumlahan Matriks**
```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

hasil = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print(hasil)   # [[6, 8], [10, 12]]
```

**b. Perkalian Matriks**
```python
def kali_matriks(A, B):
    baris_A, kolom_A = len(A), len(A[0])
    baris_B, kolom_B = len(B), len(B[0])

    if kolom_A != baris_B:
        raise ValueError("Jumlah kolom A harus sama dengan jumlah baris B")

    hasil = [[0 for _ in range(kolom_B)] for _ in range(baris_A)]

    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(kali_matriks(A, B))   # [[19, 22], [43, 50]]
```

**c. Transpose Matriks**
```python
def transpose(matriks):
    baris = len(matriks)
    kolom = len(matriks[0])
    hasil = [[matriks[j][i] for j in range(baris)] for i in range(kolom)]
    return hasil

M = [[1, 2, 3], [4, 5, 6]]
print(transpose(M))   # [[1, 4], [2, 5], [3, 6]]
```

### 4.3 Menggunakan NumPy (opsional, sebagai pembanding)
```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A + B)        # penjumlahan
print(A @ B)        # perkalian matriks
print(A.T)          # transpose
```
Menyebutkan NumPy dapat menambah nilai presentasi karena menunjukkan bahwa dalam praktik nyata, operasi matriks jarang dilakukan manual.

---

## 5. Kompleksitas Waktu (Time Complexity)

### 5.1 Tabel Kompleksitas Operasi Array (List Python)

| Operasi | Kompleksitas | Keterangan |
|---|---|---|
| Akses elemen `arr[i]` | **O(1)** | Langsung dihitung dari alamat memori |
| Update elemen `arr[i] = x` | **O(1)** | Langsung menimpa nilai di indeks tsb |
| Pencarian (Linear Search) | **O(n)** | Harus memeriksa satu per satu |
| Pencarian (Binary Search, data terurut) | **O(log n)** | Membagi dua pencarian tiap iterasi |
| Insert di akhir (`append`) | **O(1)** amortized | Kadang O(n) jika kapasitas internal penuh dan perlu realokasi |
| Insert di awal/tengah (`insert`) | **O(n)** | Elemen setelahnya harus digeser |
| Delete di akhir (`pop`) | **O(1)** | Tidak perlu pergeseran |
| Delete di awal/tengah (`pop(i)`, `remove`) | **O(n)** | Elemen setelahnya harus digeser |
| Traversal (kunjungi semua elemen) | **O(n)** | Harus melewati seluruh elemen |
| Sorting (Timsort — algoritma `sort()` Python) | **O(n log n)** | Rata-rata dan worst-case |

### 5.2 Kompleksitas Operasi Matriks (ukuran n x n)

| Operasi | Kompleksitas |
|---|---|
| Akses elemen | O(1) |
| Penjumlahan matriks | O(n²) |
| Transpose | O(n²) |
| Perkalian matriks (metode biasa) | O(n³) |
| Perkalian matriks (Strassen — lanjutan) | ≈ O(n^2.807) |

### 5.3 Kenapa Ini Penting?
Poin ini biasanya jadi bahan pertanyaan dosen: **kelebihan utama array adalah akses O(1)**, tapi **kelemahannya adalah insert/delete di tengah yang O(n)** karena elemen harus digeser. Ini kontras dengan struktur data lain seperti *linked list* yang unggul di insert/delete tapi lemah di akses acak.

---

## 6. Studi Kasus dan Penyelesaian

### Studi Kasus 1: Mencari Nilai Maksimum dan Minimum dalam Array
**Soal:** Diberikan array nilai ujian mahasiswa, tentukan nilai tertinggi dan terendah.

```python
nilai = [78, 92, 55, 88, 100, 45, 67]

def cari_max_min(arr):
    maksimum = arr[0]
    minimum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maksimum:
            maksimum = arr[i]
        if arr[i] < minimum:
            minimum = arr[i]
    return maksimum, minimum

maks, minn = cari_max_min(nilai)
print(f"Nilai tertinggi: {maks}, Nilai terendah: {minn}")
```
**Kompleksitas:** O(n) — array dilewati satu kali.

---

### Studi Kasus 2: Rotasi Array (Array 1D)
**Soal:** Putar (rotasi) elemen array ke kanan sebanyak `k` posisi.
Contoh: `[1, 2, 3, 4, 5]` dirotasi 2 posisi ke kanan → `[4, 5, 1, 2, 3]`

```python
def rotasi_array(arr, k):
    n = len(arr)
    k = k % n  # antisipasi jika k lebih besar dari panjang array
    return arr[-k:] + arr[:-k]

data = [1, 2, 3, 4, 5]
print(rotasi_array(data, 2))   # [4, 5, 1, 2, 3]
```
**Kompleksitas:** O(n) — karena membuat array baru dengan slicing.

---

### Studi Kasus 3: Transpose Matriks Nilai Siswa
**Soal:** Sebuah matriks berisi nilai 3 siswa untuk 4 mata kuliah (baris = siswa, kolom = mata kuliah). Ubah agar barisnya menjadi mata kuliah dan kolomnya menjadi siswa (transpose), untuk keperluan rekap per mata kuliah.

```python
nilai_siswa = [
    [80, 75, 90, 70],   # Siswa 1
    [85, 60, 88, 95],   # Siswa 2
    [70, 92, 77, 60]    # Siswa 3
]

def transpose(matriks):
    baris = len(matriks)
    kolom = len(matriks[0])
    hasil = [[matriks[j][i] for j in range(baris)] for i in range(kolom)]
    return hasil

rekap_matkul = transpose(nilai_siswa)
for i, matkul in enumerate(rekap_matkul):
    print(f"Mata Kuliah {i+1}: {matkul}")
```
**Output:**
```
Mata Kuliah 1: [80, 85, 70]
Mata Kuliah 2: [75, 60, 92]
Mata Kuliah 3: [90, 88, 77]
Mata Kuliah 4: [70, 95, 60]
```
**Kompleksitas:** O(n × m), di mana n = jumlah baris, m = jumlah kolom.

---

### Studi Kasus 4: Perkalian Matriks — Sistem Rekomendasi Sederhana
**Soal:** Matriks A merepresentasikan rating 2 pengguna terhadap 3 film. Matriks B merepresentasikan bobot 3 film terhadap 2 genre. Hitung skor kecocokan tiap pengguna terhadap tiap genre menggunakan perkalian matriks.

```python
# Baris = pengguna, Kolom = film
rating_pengguna = [
    [5, 3, 4],   # Pengguna 1
    [2, 5, 1]    # Pengguna 2
]

# Baris = film, Kolom = genre (Aksi, Drama)
bobot_genre = [
    [0.8, 0.2],
    [0.1, 0.9],
    [0.6, 0.4]
]

def kali_matriks(A, B):
    hasil = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil

skor = kali_matriks(rating_pengguna, bobot_genre)
print("Skor kecocokan [Aksi, Drama]:")
for i, s in enumerate(skor):
    print(f"Pengguna {i+1}: {s}")
```
**Kompleksitas:** O(n × m × p) — sesuai aturan perkalian matriks umum.

---

## 7. Ringkasan Poin Penting untuk Presentasi

1. Array = kumpulan data sejenis, disimpan berurutan, diakses via indeks → akses O(1).
2. Python tidak punya array primitif bawaan; `list` adalah representasi paling umum, `array` dan `numpy.ndarray` adalah alternatif yang lebih "murni".
3. Array 2D = array di dalam array → dasar representasi matriks.
4. Hindari jebakan `[[0]*kolom]*baris` karena masalah referensi objek.
5. Trade-off utama array: **akses cepat (O(1))** vs **insert/delete di tengah yang mahal (O(n))**.
6. Studi kasus sebaiknya dikaitkan dengan konteks nyata (nilai mahasiswa, rekomendasi, dsb) agar lebih mudah dipahami audiens.

---

*Draft ini bisa dijadikan dasar untuk menyusun slide presentasi. Setiap bagian di atas berpotensi menjadi 1–3 slide, dengan bagian kode dan studi kasus bisa disederhanakan/dipotong sesuai kebutuhan waktu presentasi.*