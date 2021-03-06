def merge(B, R, left_index, right_index):
    i = j = 0
    res = []
    while i < len(B) and j < len(R):
        if B[i] <= R[j]:
            res.append(B[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    while i < len(B):
        res.append(B[i])
        i += 1
    while j < len(R):
        res.append(R[j])
        j += 1
    print (f"{left_index} {right_index} {res[0]} {res[len(res) - 1]}")
    return res

def merge_sort(C, left_index, right_index):
    n = len(C)
    if n <= 1:
        return C
    middle = n//2
    B = merge_sort(C[0:middle], left_index, left_index+middle-1)    
    R = merge_sort(C[middle:n], left_index+middle, right_index)

    return merge(B, R, left_index, right_index)     

N = int(input())
C = list(map(int, input().split(" ")))
c = merge_sort(C, 1, N)
print(" ".join(map(str,c)))
