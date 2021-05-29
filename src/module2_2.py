def sort_pair(A, n):
    for i in range(1, n):
        for j in range(0, n-i):
            if A[j][1] < A[j+1][1]:
                A[j],A[j+1] = A[j+1],A[j]
            elif A[j][1] == A[j+1][1] and A[j][0] > A[j+1][0]:
                    A[j],A[j+1] = A[j+1],A[j]
    for i in range(0, n):
        print(" ".join(map(str,A[i])))

D = int(input())
A = [0]*D
for i in range(0, D):
    A[i] = input()
    A[i] = A[i].split(" ")
    A[i] = list(map(int,A[i]))

sort_pair(A, D)