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
        else:
            C.append(B[j])
            j += 1
    print(C[0], C[len(C)-1])
    return C
def merge_sort (m, l, r):
    if r - l == 1:
        v = []
        v.append(m[l])
        return v
    middle = int((r+l)/2)
    left = merge_sort(m, l, middle)
    right = merge_sort(m, middle ,r)
    print(l+1, r, end= " ")
    return merge(left,right)

n = int(input())

    
m=[float(i) if i.find(".")!=-1 else int(i) for i in input().split(" ")]
ans = merge_sort(m, 0, len(m))
for i in ans:
    print(i, end=' ')
print()
