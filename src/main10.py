def merge(Q, R):
    i = j = 0
    inversions = 0
    res = []
    while i < len(Q) and j < len(R):
        if Q[i] <= R[j]:
            res.append(Q[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
            inversions += len(Q) - i
    while i < len(Q):
        res.append(Q[i])
        i += 1
    while j < len(R):
        res.append(R[j])
        j += 1
    return res, inversions

def merge_sort(B):
    n = len(B)
    if n <= 1:
        return B, 0
    middle = n//2
    Q, l_inversions = merge_sort(B[0:middle])    
    R, r_inversions = merge_sort(B[middle:n])
    res, inversions = merge(Q, R)
    return res, inversions + l_inversions + r_inversions     

N = int(input())
B = list(map(int, input().split(" ")))
B, total_inversions = merge_sort(B)
print(total_inversions)

