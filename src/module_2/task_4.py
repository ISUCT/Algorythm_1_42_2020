def merge(left_arr, right_arr):
    new_lst = [] 
    inv = 0
    i = 0
    j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            new_lst.append(left_arr[i])
            i += 1
        else:
            new_lst.append(right_arr[j])
            j += 1
            inv += len(left_arr) - i

    while i < len(left_arr):
        new_lst.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        new_lst.append(right_arr[j])
        j += 1

    return new_lst, inv

def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr)//2
        left, inv_l = mergeSort(arr[:mid])
        right, inv_r = mergeSort(arr[mid:]) 
        sorted_arr, inv = merge(left, right)
        return sorted_arr, inv + inv_l + inv_r

def task_4_sorting():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['1','1']))  # input
    >>> task_4_sorting()
    0
    >>> sys.stdin = io.StringIO(chr(10).join(['2','3 1']))  # input
    >>> task_4_sorting()
    1
    >>> sys.stdin = io.StringIO(chr(10).join(['5','5 4 3 2 1']))  # input
    >>> task_4_sorting()
    10
    """ 

    n = int(input())
    arr = [int(i) for i in input().split()]
    arr, inversions = mergeSort(arr)
    print(inversions)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)