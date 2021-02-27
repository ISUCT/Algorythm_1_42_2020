def merge (A,B):
    i = 0
    j = 0
    C = [0 for _ in range(len(A)+len(B))]
    for k in range(len(A)+len(B)):
        if i == len(A):
            C[j] = B[j]
            j += 1
        elif j == len(B):
            C[i] = A[i]
            i += 1

def merge_sort (m, l, r):
    if r - l:
        v = [0]
        v[0] = m[l]
        return v
    middle = (r+l)/2
    right = merge_sort(m, middle ,r)
    left = merge_sort(m, l, middle)
    return merge(left,right)

m = [int(input()) for _ in range(int(input()))
print(merge_sort(m, 0, len(m)))