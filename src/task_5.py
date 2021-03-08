def task_5_sorting():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['5','1 0 1 2 0']))  # input
    >>> task_5_sorting()
    3
    """ 
    n = input()
    lst = []
    arr = input().split(" ")
    for i in arr:
        if i not in lst:
            lst.append(i) 
    print(len(lst))
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)






