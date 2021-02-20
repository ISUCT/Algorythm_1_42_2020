def pr(m):
    for i in range(len(m)):
        print(m[i], end =' ')
    print()

n = int(input())
m = [int(i) for i in input().split(" ")]
prs = 0
if n == 1:
    print(m[0])
else:
    prs = 1
i = 0
c = 0
k = 0
while prs:
    if m[i+1]<m[i]:
        m[i],m[i+1] = m[i+1],m[i]
        c += 1
        pr(m)
        k += 1
    if i == n-2 and c == 0:
        break
    elif i==n-2:
        i = -1
        c = 0
    i += 1
if k == 0 and prs == 0:
    for i in range(len(m)):
        print(m[i], end =' ')
    print()