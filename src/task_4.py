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
    k = 0
    arr = [int(i) for i in input().split()]
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                k += 1
    print(k)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)




