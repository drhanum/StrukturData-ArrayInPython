import array
import numpy as np

# List: bisa campur tipe data
list_contoh = [1, "dua", 3.0, True]

# array.array: harus 1 tipe data (misal 'i' = integer)
array_contoh = array.array('i', [1, 2, 3, 4])

# numpy.array: bisa campur tipe data, tapi akan diubah ke tipe data yang sama
numpy_array_contoh = np.array([1, 2.1, 3, 4])

print(list_contoh)
print(array_contoh)
print(numpy_array_contoh)