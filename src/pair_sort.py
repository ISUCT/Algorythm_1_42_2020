def pair_sorting():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['3','101 80','305 90', '200 14']))  # input
    >>> pair_sorting()
    305 90
    101 80
    200 14
    >>> sys.stdin = io.StringIO(chr(10).join(['3','20 80','30 90', '25 90']))  # input
    >>> pair_sorting()
    25 90
    30 90
    20 80
    """   
    n = int(input())
    arr = []
    lst = []
    for i in range(0 , n):
        arr = input().split(" ") 
        lst.append([])
        for item in arr:
            lst[i].append(int(item))
    for j in range(n):
        for i in range(n-1):
            if(lst[i][1] < lst[i+1][1]):
                lst[i][0],lst[i+1][0] = lst[i+1][0],lst[i][0]
                lst[i][1],lst[i+1][1] = lst[i+1][1],lst[i][1]
            if(lst[i][1] == lst[i+1][1]):
                if(lst[i][0] > lst[i+1][0]):
                    lst[i][0],lst[i+1][0] = lst[i+1][0],lst[i][0]
                    lst[i][1],lst[i+1][1] = lst[i+1][1],lst[i][1]
    for i in range(n):    
        print(str(lst[i][0]) + " " + str(lst[i][1]))
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)