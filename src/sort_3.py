def merge (A,B):
    i = 0
    j = 0
    C = []
    for k in range(len(A)+len(B)):
        if i == len(A):
            C.append(B[j])
            j += 1
        elif j == len(B):
            C.appne(A[i])
            i += 1
        elif A[i] < B[j]:
            C.appne(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    return C
def merge_sort (m, l, r):
    if r - l:
        v = []
        v.append(m[l])
        return v
    middle = int((r+l)/2)
    right = merge_sort(m, middle ,r)
    left = merge_sort(m, l, middle)
    return merge(left,right)

n = int(input())
m = [int(i) for i in input().split(" ")]
ans = merge_sort(m, 0, len(m))
print(ans)