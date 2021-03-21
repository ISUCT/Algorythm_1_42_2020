Q = int(input())
H = list(map(int, input().split(" ")))
s = int(input())
X = list(map(int, input().split(" ")))
def m(a, b, n):
    mass = [0]*(n+1)
    for j in b:
        mass[j] = mass[j]+1
    for i in range(n):
        if a[i] >= mass[i+1]:
            print("no")
        else:
            print("yes")
m(H, X, Q)