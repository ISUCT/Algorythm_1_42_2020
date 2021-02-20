#С помощью пузырьковой сортировки:
def sort_pair_bubble(A, n):
    for i in range(0, N):
        A[i] = list(map(int, input().split(" ")))
    for i in range(1, n):
        for j in range(0, n-i):
            if A[j][1] < A[j+1][1]:
                A[j],A[j+1] = A[j+1],A[j]
            elif A[j][1] == A[j+1][1] and A[j][0] > A[j+1][0]:
                    A[j],A[j+1] = A[j+1],A[j]
    for i in range(0, n):
        print(" ".join(map(str,A[i])))

#C помощью сортировки вставками:
def sort_pair_insert(A, n):
    A[0] = list(map(int, input().split(" "))) 
    for i in range(1, n):          
        if n == 1:
            print(" ".join(map(str, A[0])))
            return
        A[i] = list(map(int, input().split(" ")))
        for j in range(i, 0, -1):
            if A[j][1] > A[j-1][1]:
                A[j],A[j-1] = A[j-1],A[j]
            elif A[j][1] == A[j-1][1] and A[j][0] < A[j-1][0]:
                    A[j],A[j-1] = A[j-1],A[j]
    for i in range(0, n):
        print(" ".join(map(str, A[i])))
        
N = int(input())
A = [0]*N
sort_pair_insert(A, N)