def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr, 0
    mid = n//2
    left, left_inv = merge_sort(arr[:mid])    
    right, right_inv = merge_sort(arr[mid:])
    res, k = sort(left, right)
    s = k + left_inv + right_inv
    return res, s

def sort(left, right):
    k = 0
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            k += len(left) - i
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res, k    

n = int(input())
arr = list(map(int, input().split(" ")))
arr, inversions = merge_sort(arr)
print(inversions)