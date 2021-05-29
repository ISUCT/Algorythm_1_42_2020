def prefix_func(string,length):
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
    >>> sys.stdin = io.StringIO(chr(10).join(['aaaaa']))  # input
    >>> main()
    5
    >>> sys.stdin = io.StringIO(chr(10).join(['abcabcabc']))  # input
    >>> main()
    3
    >>> sys.stdin = io.StringIO(chr(10).join(['abab']))  # input
    >>> main()
    2
    """
    s = str(input())
    length = len(s)
    result = prefix_func(s,length)
    result = length - result[-1]
    
    if (length % result == 0):
        print(length // result)
    else:
        print('1')

if __name__ == "__main__":
   import doctest
   doctest.testmod(verbose=True)