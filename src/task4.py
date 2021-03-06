def m(a, b, n):
    arr = [0]*(n+1)
    for it in b:
        arr[it] += 1
    for i in range(n):
        if a[i] >= arr[i+1]:
            print("no")
        else:
            print("yes")
G = int(input())
U = list(map(int, input().split(" ")))
p = int(input())
L = list(map(int, input().split(" ")))
m(U, L, G)
 