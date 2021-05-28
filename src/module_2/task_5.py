def counting_sort(lst, max_num, k):
    sorting_arr = [0]*(max_num + 1)
    for i in range(len(lst)):
        sorting_arr[lst[i]] = sorting_arr[lst[i]] + 1
    for item in sorting_arr:
        if item != 0:
            k += 1
    sorting_arr[0] = sorting_arr[0] - 1
    for i in range(1, max_num + 1):
        sorting_arr[i] = sorting_arr[i] + sorting_arr[i - 1]
 
    rst = [None]*len(lst)
 
    for x in reversed(lst):
        rst[sorting_arr[x]] = x
        sorting_arr[x] = sorting_arr[x] - 1
 
    return rst, k
def task_5_sorting():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['10','1 2 -2 1 -1 -1 0 2 0 0']))  # input
    >>> task_5_sorting()
    5
    >>> sys.stdin = io.StringIO(chr(10).join(['5','1 0 1 2 0']))  # input
    >>> task_5_sorting()
    3
    """ 
    n = int(input())
    k = 0
    arr = [int(i) for i in input().split()]
    lst = [[],[]]
    for item in arr:
        if item >= 0:
            lst[0].append(item)
        else:
            lst[1].append(item)
    if len(lst[0])>0:
        lst[0], k = counting_sort(lst[0], abs(max(lst[0])), k)
    if len(lst[1])>0:
        lst[1], k = counting_sort(lst[1], abs(min(lst[1])), k)
    print(k)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)




