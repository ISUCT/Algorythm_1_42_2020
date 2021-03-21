def merge_sort(A, left_index, right_index):
    n = len(A)
    if n <= 1:
        return A
    middle = n//2
    L = merge_sort(A[0:middle], left_index, left_index+middle-1)    
    R = merge_sort(A[middle:n], left_index+middle, right_index)
    i = j = 0
    res = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    while i < len(L):
        res.append(L[i])
        i += 1
    while j < len(R):
        res.append(R[j])
        j += 1
    print (f"{left_index} {right_index} {res[0]} {res[len(res) - 1]}")
    return res 

N = int(input())
A = list(map(int, input().split()))
A = merge_sort(A, 1, N)
print(" ".join(map(str,A)))