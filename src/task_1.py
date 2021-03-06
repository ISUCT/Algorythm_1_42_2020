def task_1_sorting():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['4','4 3 2 1']))  # input
    >>> task_1_sorting()
    3 4 2 1
    3 2 4 1
    3 2 1 4
    2 3 1 4
    2 1 3 4
    1 2 3 4
    """
    n = int(input())
    res = input()
    arr = []
    num = True
    res_str = res.split(" ")
    for item in res_str:
        arr.append(int(item))
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                num = False
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
                print(" ".join(map(str, arr)))
    if num == True:
        print(0)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)