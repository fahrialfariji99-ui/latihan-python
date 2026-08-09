# Membuat matriks A sesuai pola
n = 4
A = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        A[i][j] = j + 1   # angka mengikuti kolom (1,2,3,4)

# Menampilkan matriks
for baris in A:
    print(*baris)