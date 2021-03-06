def radix_sort(B, n):
    digit = len(B[0])
    for i in range(digit):
        buckets_arr = [[] for j in range(10)]
        for item in B:
            index = int(item)//10**i % 10
            buckets_arr[index].append(item)
        print("Phase", i+1)
        B=[]
        for i in range(10):
            print(f"Bucket {i}: ", end="")
            print(", ".join(buckets_arr[i]) if len(buckets_arr[i])>0 else "empty")
            B = B + buckets_arr[i]
        print("**********")
    return B

N = int(input())
B = []
for i in range(N):
    B.append(input())
print("Initial array:")
print(", ".join(B))
print("**********")
B = radix_sort(B, N)
print("Sorted array:")
print(", ".join(B))
