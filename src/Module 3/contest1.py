def func_hash(t_str, s_str):
    p = 31
    m = 1
    q = 2 ** 31 - 1
    m = 1
    hash = 0
    s1_hash = 0
    useless_variable = 1
    res = []
 
    for i in s_str[::-1]:
        s1_hash += ord(i) * m
        m *= p
        s1_hash %= q
        m %= q
 
    for i in t_str[:len(s_str)][::-1]:
        hash += m * ord(i)
        m *= p
        hash %= q
        m %= q
 
    for i in range(len(s_str) - 1):
        useless_variable *= p
        useless_variable %= q
 
    if hash == s1_hash: res.append(0)
    for i in range(1, len(t_str) - len(s_str) + 1):
        new_hash = ((hash % q - ord(t_str[i - 1]) * useless_variable % q) * p % q + ord(t_str[i + len(s_str) - 1])) % q
        if new_hash == s1_hash: 
            res.append(i)
        hash = new_hash
    return res

def main(): 
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['ababbababa','aba']))  # input
    >>> main()
    0 5 7
    """
    t_str = input()
    s_str = input()  
    result = func_hash(t_str,s_str)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)