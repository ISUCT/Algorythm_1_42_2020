def merge_sort(a, ind_left, ind_right):
    n = len(a)
    if n < 2:
        return a
    arr = []
    between = n//2
    left = merge_sort(a[:between], ind_left, ind_left + between - 1)
    right = merge_sort(a[between:], between + ind_left, ind_right)
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j +=1
    while i < len(left):
        arr.append(left[i])
        i += 1
    while j < len(right):
        arr.append(right[j])
        j += 1
    print (ind_left, ind_right, arr[0], arr[len(arr) - 1])
    return arr

n = int(input())
a = list(map(int, input().split()))
b = merge_sort(a, 1, n)
print(' '.join(map(str, b)))