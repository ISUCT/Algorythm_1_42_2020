def merge_sort(M, left_index, right_index):
    n = len(M)
    if n <= 1:
        return M
    middle = n//2
    L = merge_sort(M[0:middle], left_index, left_index+middle-1)    
    R = merge_sort(M[middle:n], left_index+middle, right_index)
    i = j = 0
    res = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            res.append(L[i])
            i += 1
        else:
        res.append(R[j])
        j += 1
    print (f"{left_index} {right_index} {res[0]} {res[len(res) - 1]}")
    return res 
N = int(input())
M = list(map(int, input().split()))
M = merge_sort(M, 1, N)
print(" ".join(map(str,M)))
def merge(L, R):
    i = j = 0
    inversions = 0