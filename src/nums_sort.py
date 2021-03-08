n = int(input())
m = list(map(int, input().split()))
x = 0
m.sort()
for i in range(n-1):
    if m[i] != m[i+1]:
        x +=1
print(x+1)
