def radix_sort(A, n):
    digit = len(A[0])
    for i in range(digit):
        buckets_arr = [[] for j in range(10)]
        for item in A:
            index = int(item)//10**i % 10
            buckets_arr[index].append(item)
        print("Phase", i+1)
        A=[]
        for i in range(10):
            print(f"Bucket {i}: ", end="")
            print(", ".join(buckets_arr[i]) if len(buckets_arr[i])>0 else "empty")
            A = A + buckets_arr[i]
        print("**********")
    return A

N = int(input())
A = []
for i in range(N):
    A.append(input())
print("Initial array:")
print(", ".join(A))
print("**********")
A = radix_sort(A, N)
print("Sorted array:")
print(", ".join(A))