def Sort(Arr, Num):
    List = [0]*Num
    return merge_sort(Arr, List, 0, Num-1)

def merge_sort(Arr, List, left, right):
    Meter = 0
    if left < right:
        mid = (left + right)//2
        Meter += merge_sort(Arr, List, left, mid)
        Meter += merge_sort(Arr, List, mid + 1, right)
        Meter += Merge(Arr, List, left, mid, right)
    return Meter

def Merge(Arr, List, left, mid, right):
    i = left     
    j = mid + 1 
    u = left     
    Meter = 0
    while i <= mid and j <= right:
        if Arr[i] <= Arr[j]:
            List[u] = Arr[i]
            u += 1
            i += 1
        else:
            List[u] = Arr[j]
            Meter += (mid-i + 1)
            u += 1
            j += 1
    while i <= mid:
        List[u] = Arr[i]
        u += 1
        i += 1
    while j <= right:
        List[u] = Arr[j]
        u += 1
        j += 1
    for now in range(left, right + 1):
        Arr[now] = List[now]    
    return Meter

Quantity = int(input())
Arr = list(map(int, input().split())) 
Num = len(Arr)
Arr = Sort(Arr, Num)
print(Arr) 