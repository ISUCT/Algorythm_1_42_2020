def prefix_func(string, length):
    cnt = [0] * length 
    for i in range (length - 1):
        j = cnt[i]
        while (j > 0) and (string[i + 1] != string[j]):
            j = cnt[j - 1]
        if (string[i + 1] == string[j]):
            cnt[i+1] = j + 1
        else:
            cnt[i + 1] = 0
    return cnt

def main():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['z']))  # input
    >>> main()
    1
    """
    s = str(input())
    length = len(s)
    result = prefix_func(s, length)
    print(length - result[-1])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
