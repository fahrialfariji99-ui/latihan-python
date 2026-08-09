M = [19, 3, 7, 4, 13, 8, 20]
P = 4

posisi = -1
for i in range(len(M)):
    if M[i] == P:
        posisi = i
        break

if posisi != -1:
    print("1. Nilai", P, "ditemukan pada indeks:", posisi)
else:
    print("1. Nilai", P, "tidak ditemukan")


# 2. Best Case Sorting pada list X
X = [6, 9, 12, 18, 22, 65, 44]

sorted_min_max = sorted(X)             
sorted_max_min = sorted(X, reverse=True) 

print("\n2. Urutan min → max:", sorted_min_max)
print("   Urutan max → min:", sorted_max_min)


# 3. Worst Case Sorting pada list C
C = [55, 46, 30, 24, 18, 10, 18, -3]

sorted_min_max_C = sorted(C)                
sorted_max_min_C = sorted(C, reverse=True)  

print("\n3. Urutan min → max:", sorted_min_max_C)
print("   Urutan max → min:", sorted_max_min_C)
