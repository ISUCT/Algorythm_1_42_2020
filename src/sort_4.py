
def merge (A,B):
    i = 0
    j = 0
    C = []
    for k in range(len(A)+len(B)):
        if i == len(A):
            C.append(B[j])
            j += 1
        elif j == len(B):
            C.append(A[i])
            i += 1
        elif A[i] < B[j]:
            C.append(A[i])
            i += 1
            if i>j:
                print(B[j],A[i], end=" # ")
        elif A[i] > B[j] and i<j:
            print(A[i],B[j], end=" # ")
        else:
            C.append(B[j])
            j += 1
    return C
def merge_sort (m, l, r):
    if r - l == 1:
        v = []
        v.append(m[l])
        return v
    middle = int((r+l)/2)
    left = merge_sort(m, l, middle)
    right = merge_sort(m, middle ,r)
    return merge(left,right)

n = int(input())
m = [int(i) for i in input().split(" ")]
ans = merge_sort(m, 0, len(m))
for i in ans:
    print(i, end=' ')
print()