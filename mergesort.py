# def mergeSort(X):
#     print("Bilangan diurutkan ",X)
#     if len(X)>1:
#         mid = len (X)//2
#         lefthalf = X[:mid]
#         righthalf = X[mid:]
#         mergeSort(lefthalf)
#         mergeSort(righthalf)
#         i=j=k=0
#         while 1 < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 X[k]=lefthalf[i]
#                 i=i+1
#             else:
#                 X[k]= righthalf[j]
#                 j=j+1
#         k=k+1
#         while i < len(lefthalf):
#             X[k]=lefthalf[i]
#             i=i+1
#             k=k+1
#         while j <len(righthalf):
#             X[k]=righthalf[i]
#             X[k]=righthalf[j]
#             j=j+1
#             k=k+1
#         print("Merging ", X)
# X =[22,10,15,3,8,2]
# mergeSort(X)
# print(X)

def mergeSort(X):
    print("Bilangan diurutkan:", X)

    if len(X) > 1:
        mid = len(X) // 2
        lefthalf = X[:mid]
        righthalf = X[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0

        # Merge kedua bagian
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                X[k] = lefthalf[i]
                i += 1
            else:
                X[k] = righthalf[j]
                j += 1
            k += 1

        # Jika masih ada sisa di lefthalf
        while i < len(lefthalf):
            X[k] = lefthalf[i]
            i += 1
            k += 1

        # Jika masih ada sisa di righthalf
        while j < len(righthalf):
            X[k] = righthalf[j]
            j += 1
            k += 1

        print("Merging:", X)


X = [22, 10, 15, 3, 8, 2]
mergeSort(X)
print("Hasil akhir:", X)
