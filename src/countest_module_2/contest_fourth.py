def Sort(A, Num):
    List = [0]*Num
    return merge_sort(A, List, 0, Num-1)
 
def merge_sort(A, List, left, right):
    Count = 0
    if left < right:
        mid = (left + right)//2
        Count += merge_sort(A, List, left, mid)
        Count += merge_sort(A, List, mid + 1, right)
        Count += Merge(A, List, left, mid, right)
    return Count
 
def Merge(A, List, left, mid, right):
    i = left     
    j = mid + 1 
    b = left     
    Count r = 0
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            List[b] = A[i]
            b += 1
            i += 1
        else:
            List[b] = A[j]
            Count += (mid-i + 1)
            b += 1
            j += 1
    while i <= mid:
        List[b] = A[i]
        b += 1
        i += 1
    while j <= right:
        List[b] = A[j]
        b += 1
        j += 1
    for now in range(left, right + 1):
        A[now] = List[now]    
    return Count
 
q = int(input())
A= list(map(int, input().split())) 
Num = len(A)
A = Sort(A, Num)
print(A)