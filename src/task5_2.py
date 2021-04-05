def counting_sort(lst, n, k):
    arr = [0]*(n + 1)
    for i in range(len(lst)):
        arr[lst[i]] += 1
    for item in arr:
        if item != 0:
            k += 1
    arr[0] -= 1
    for i in range(1, n + 1):
        arr[i] += arr[i - 1]

    res = [None]*len(lst)

    for x in reversed(lst):
        res[arr[x]] = x
        arr[x] -= 1
    return res, k

def sort():
    n = int(input())
    k = 0
    a = [int(i) for i in input().split()]
    lst = [[],[]]
    for item in a:
        if item >= 0:
            lst[0].append(item)
        else:
            lst[1].append(item)
    if len(lst[0])>0:
        lst[0], k = counting_sort(lst[0], abs(max(lst[0])), k)
    if len(lst[1])>0:
        lst[1], k = counting_sort(lst[1], abs(min(lst[1])), k)
    print(k)
sort()