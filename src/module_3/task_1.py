def prefix_function(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i-1]
        while (k > 0 and s[k] != s[i]):
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p[i] = k
    return p


def task_1():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['ababbababa','aba']))  # input
    >>> task_1()
    0 5 7
    """
    S = input()
    T = input()
    arr = []
    S_T = T + '|' + S
    S_T = prefix_function(S_T)
    for i in range(len(S_T)):
        if S_T[i] == len(T):
            arr.append(str(i - 2*len(T)))
    lst = ' '.join(arr)
    print(lst)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)