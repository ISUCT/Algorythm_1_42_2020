def inversion_sorting():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['1','1']))  # input
    >>> inversion_sorting()
    0
    >>> sys.stdin = io.StringIO(chr(10).join(['2','3 1']))  # input
    >>> inversion_sorting()
    1
    >>> sys.stdin = io.StringIO(chr(10).join(['5','5 4 3 2 1']))  # input
    >>> inversion_sorting()
    10
    """ 
    lst = []
    inv = 0
    for i in range(2):
        arr = input().split(" ")
        lst.append([])
        for item in arr:
            lst[i].append(int(item))
    if lst[0][0] != 1:
        for i in range(0, lst[0][0]):
            if i !=  lst[0][0] - 1 - i:      
                lst[1][i],lst[1][lst[0][0] - 1 - i] = lst[1][lst[0][0] - 1 - i],lst[1][i]
                print(lst)
                inv+=1  
            if i == lst[0][0] - 1 - i:
                for n in range(0, i -1):
                    lst[1][n],lst[1][n + 1] = lst[1][n+1],lst[1][n]
                    inv+=1
                #for k in range(i + 1, lst[0][0]):
                    #lst[1][i],lst[1][lst[0][0] - 1 - i] = lst[1][lst[0][0] - 1 - i],lst[1][i]  
    print(inv)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)




