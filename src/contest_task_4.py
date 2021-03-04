#Не проходит на контесте
def merge(L, R):
    i = j = 0
    inversions = 0
    res = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
            inversions += len(L) - i
    while i < len(L):
        res.append(L[i])
        i += 1
    while j < len(R):
        res.append(R[j])
        j += 1
    return res, inversions

def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A, 0
    middle = n//2
    L, l_inversions = merge_sort(A[0:middle])    
    R, r_inversions = merge_sort(A[middle:n])
    res, inversions = merge(L, R)
    return res, inversions + l_inversions + r_inversions     

N = int(input())
A = list(map(int, input().split(" ")))
A, total_inversions = merge_sort(A)
print(total_inversions)