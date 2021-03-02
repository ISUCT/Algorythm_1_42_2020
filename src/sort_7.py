A = [input() for _ in range(int(input()))]
m = len(A[0])
for i in range(m-1,1,-1):
    bucket = [[''] for _ in range(26)]
    for j in range(len(A)):
        bucket[A[j][i] - 'a'].append(A[j])
    p = 0
    for j in range(26):
        for k in range(len(bucket[j])):
            A[p] = bucket[j][k]
            p += 1
for i in A:
    print(i, end=" ")
print()