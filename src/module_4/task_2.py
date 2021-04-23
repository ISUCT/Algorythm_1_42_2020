def task_2():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['3','3 2 1']))  # input
    >>> task_2()
    YES
    >>> sys.stdin = io.StringIO(chr(10).join(['4','4 1 3 2']))  # input
    >>> task_2()
    YES
    >>> sys.stdin = io.StringIO(chr(10).join(['3','2 3 1']))  # input
    >>> task_2()
    NO
    """
    length = int(input())
    T_A = list(map(int,input().split()))
    T_B = []
    Stack = []
    test =  sorted(T_A)
    for i in range(length):
        if (Stack == []) or (Stack[-1] > T_A[0]):
            Stack.append(T_A[0])
            T_A.pop(0)
        else:
            while (Stack != [] and Stack[-1] < T_A[0]):
                T_B.append(Stack[-1])
                Stack.pop(-1)
            if (Stack == []) or (Stack[-1] > T_A[0]):
                Stack.append(T_A[0])
                T_A.pop(0)        
    if Stack != []: 
        for i in range(len(Stack)):
            T_B.append(Stack[-1])
            Stack.pop(-1)   
    if T_B == test:
        print("YES")
    else: 
        print("NO")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)