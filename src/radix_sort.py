def radix_sort(L, n):
    mas = len(L(0))
    length = len(str(max(L)))
    for i in range(mas):
        arr = [[] for j in range(10)]
        L=[]
        for item in L:
            index = int(item)//10**i % 10
            arr[index].append(item)
        print("Phase 1", i+1)
        for i in range(10):
            print(f"Bucket {i}: ", end="")
            print(", ".join(arr[i]) if len(arr[i])>0 else "empty")
            L = L + arr[i]
        print("**********")
    return L

N = int(input())
L = []
for i in range(N):
    L.append(input())
print("Initial array:")
print(", ".join(L))
print("**********")
L = radix_sort(L, N)
print("Sorted array:")
print(", ".join(L))


