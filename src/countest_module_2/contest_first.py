q = int(input())
A = list(map(int,input().split(" ")))
C = 0
for i in range(q-1):
   for j in range(q-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            C += 1
            print(' '.join(map(str, A)))
if C == 0:
    print(C)