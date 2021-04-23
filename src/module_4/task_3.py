def task_3():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['10','1 2 3 2 1 4 2 5 3 1']))  # input
    >>> task_3()
    -1 4 3 4 -1 6 9 8 9 -1 
    """
    l = int(input())
    a = list(zip(list(map(int, input().split())), range(l)))
    Stack = []
    rst = [0]*l
    for i in reversed(a):
        while (Stack != []) and (Stack[-1][0] >= i[0]):
            Stack.pop()
        if Stack == []:
            rst[i[1]] = -1
        else:
            rst[i[1]] = Stack[-1][1]
        Stack.append(i)
    print(' '.join(map(str, rst))) 

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) 
