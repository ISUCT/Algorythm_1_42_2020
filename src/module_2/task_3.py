def merge(arr, lst):
    new_lst = [] 
    i, j = 0, 0
    while i < len(arr) and j < len(lst):
        if arr[i] < lst[j]:
            new_lst.append(arr[i])
            i += 1
        else:
            new_lst.append(lst[j])
            j += 1
    while i < len(arr):   
        new_lst.append(arr[i])
        i += 1
    while j < len(lst):
        new_lst.append(lst[j])
        j += 1

    return new_lst 

def mergeSort(arr, indx):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr)//2
        left = mergeSort(arr[:mid], [indx[0],indx[0]+mid])
        right = mergeSort(arr[mid:],[indx[0]+mid, indx[1]]) 

        sort = merge(left, right)
        print(indx[0]+1, indx[1], sort[0], sort[-1])  
        return sort
def task_3_sorting():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['1','1']))  # input
    >>> task_3_sorting()
    1
    >>> sys.stdin = io.StringIO(chr(10).join(['2','3 1']))  # input
    >>> task_3_sorting()
    1 2 1 3
    1 3 
    >>> sys.stdin = io.StringIO(chr(10).join(['5','5 4 3 2 1']))  # input
    >>> task_3_sorting()
    1 2 4 5
    4 5 1 2
    3 5 1 3
    1 5 1 5
    1 2 3 4 5 
    """
    n = int(input())
    arr = list(map(int, input().split())) 
    arr = mergeSort(arr,[0, n])
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
