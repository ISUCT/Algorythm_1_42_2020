def warehouse_sorting():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['5','1 50 3 4 3','16','1 2 3 4 5 1 3 3 4 5 5 5 5 5 4 5']))  # input
    >>> warehouse_sorting()
    yes
    no
    no
    no
    yes
    """
    lst = []
    for i in range(4):
        arr = input().split(" ")
        lst.append([])
        for item in arr:
            lst[i].append(int(item))   
    for i in range(lst[0][0]):
        n = lst[3].count(i+1)
        for j in range(n):
            lst[1][i] -= 1
        if(lst[1][i] < 0):
            lst[1][i] = "yes"
            print(lst[1][i])
        else:
            lst[1][i]= "no"
            print(lst[1][i])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)