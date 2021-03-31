N = int(input())
A = [0]*N

def pair_sort(A, N):
    A[0] = list(map(int, input().split(" "))) 
    for i in range(1, N):          
        if N == 1:
            print(" ".join(map(str, A[0])))
            return
        A[i] = list(map(int, input().split(" ")))
        for j in range(i, 0, -1):
            if A[j][1] > A[j-1][1]:
                A[j],A[j-1] = A[j-1],A[j]
            elif A[j][1] == A[j-1][1] and A[j][0] < A[j-1][0]:
                    A[j],A[j-1] = A[j-1],A[j]
    for i in range(0, N):
        print(" ".join(map(str, A[i])))

pair_sort(A, N)