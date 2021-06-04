n=int(input())
numbers=list(map(int,input().split()))
massiv=[]
idx=[0]*n
d={i:numbers[i] for i in range(n)}
for i in range(n-1,-1,-1):
    while massiv and massiv[-1][1]>=d[i]:
        massiv.pop()
    if not massiv:
        idx[i]=-1
    else:
        idx[i]=massiv[-1][0]
    massiv.append([i,d[i]])
print(*idx)