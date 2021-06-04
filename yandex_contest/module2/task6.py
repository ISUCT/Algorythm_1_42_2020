n = int(input())
c = list(map(int,input().split()))
k = int(input())
p = list(map(int,input().split()))
s = [0]*max(p)
for i in p:
    s[i-1] += 1
for i in range(n):
        if c[i] >= s[i]:
            print("no")
        else:
            print("yes")
