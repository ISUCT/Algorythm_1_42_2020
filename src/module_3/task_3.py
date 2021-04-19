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

def task_3():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['aaaaa']))  # input
    >>> task_3()
    5
    >>> sys.stdin = io.StringIO(chr(10).join(['abcabcabc']))  # input
    >>> task_3()
    3
    >>> sys.stdin = io.StringIO(chr(10).join(['abab']))  # input
    >>> task_3()
    2
    """
    S = input()
    T = ""
    n = 0
    L = prefix_function(S) 
    for i in range(0, len(S)):
        if(L[i] != 0):
            break
        T += S[i]
    S_T = T + '|' + S
    S_T = prefix_function(S_T)
    for i in range(len(T), len(S_T)):
        if(S_T[i] == 1):
            n += S_T[i]
    print(n)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)