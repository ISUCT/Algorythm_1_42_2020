global c
c = 0
def merge (A,B):
    i = 0
    j = 0
    C = []
    global c
    for k in range(len(A)+len(B)):
        if i == len(A):
            C.append(B[j])
            j += 1
            c+=1
        elif j == len(B):
            C.append(A[i])
            i += 1
            c+=1
        elif A[i] < B[j]:
            C.append(A[i])
            i += 1
            c += 1
        else:
            C.append(B[j])
            j += 1
    # G=[C[i] for i in range(len(C)-1,-1,-1)]
    # for i in range(len(G)):
    #     for j in range(i+1,len(G)):
    #         if G[i]>G[j] and j > i:
    #             c += 1
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
print(c)