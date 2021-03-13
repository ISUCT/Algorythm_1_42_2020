def radix_sort(L, n):
    mas = len(L[0])
    for i in range(mas):
        radix_arr = [[] for j in range(10)]
        for item in L:
            index = int(item)//10**i % 10
            radix_arr[index].append(item)
        print("Phase", i+1)
        L = []
        for i in range(10):
            print("Bucket ", i ,":", sep = "", end=" ")
            print(", ".join(radix_arr[i]) if len(radix_arr[i])>0 else "empty")
            L = L + radix_arr[i]
        print("**********")
    return L

n = int(input())
L = []
for i in range(n):
    L.append(input())
print("Initial array:")
print(", ".join(L))
print("**********")
L = radix_sort(L, n)
print("Sorted array:")
print(", ".join(L))