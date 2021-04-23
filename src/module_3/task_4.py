def prefix_function(s):
    l = len(s)
    Counter = [0] * l    
    Counter[0] = 0
    for i in range (l - 1):
        j = Counter[i]
        while (j > 0) and (s[i + 1] != s[j]):
            j = Counter[j - 1]
        if (s[i + 1] == s[j]):
            Counter[i+1] = j + 1
        else:
            Counter[i + 1] = 0
    return Counter
def task_4():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['z']))  # input
    >>> task_4()
    1
    """
txt = str(input())
s = list(txt)
l = len(s)
prefix = prefix_function(s)
print(l - prefix[-1])
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
