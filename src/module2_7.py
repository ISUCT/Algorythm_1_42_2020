def sort(a, n):
    num = len(a[0])
    rang = 10
    for i in range(num):
        arr = [[] for j in range(rang)]
        for item in a:
            index = int(item)//10**i % 10
            arr[index].append(item)
        print("Phase", i+1)
        a=[]
        for i in range(rang):
            print(f"Bucket {i}: ", end="")
            print(", ".join(arr[i]) if len(arr[i]) > 0 else "empty")
            a += arr[i]
        print("**********")
    return a

n = int(input())
a = []
for i in range(n):
    a.append(input())
print("Initial array:")
print(", ".join(a))
print("**********")
a = sort(a, n)
print("Sorted array:")
print(", ".join(a)) 