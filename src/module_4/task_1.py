def func_psp(l):
    Counter = 0
    lst = []
    for i in l:
        if (i == '('):
            lst.append(i)
        elif (lst != []) and (lst[-1] == '('):
            lst.pop()
        else:
            Counter += 1
    return Counter + len(lst)
def task_1():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['())(()']))  # input
    >>> task_1()
    2
    >>> sys.stdin = io.StringIO(chr(10).join(['))(((']))  # input
    >>> task_1()
    5
    """
    l = str(input())
    print(func_psp(l))
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)