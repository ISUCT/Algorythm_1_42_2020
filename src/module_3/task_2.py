def String_1_2(string_2, string_1, q):

    if string_1 == string_2: 
        return 0

    string_1 += string_1

    p = 11
    m = 1
    Hash_s = 0
    for i in string_2[::-1]:
        Hash_s += ord(i) * m
        m *= p
        Hash_s %= q
        m %= q

    m = 1
    Hash = 0
    for i in string_1[:len(string_2)][::-1]:
        Hash += m * ord(i)
        m *= p
        Hash %= q
        m %= q

    Hash_t = 1
    for i in range(len(string_2) - 1):
        Hash_t *= p
        Hash_t %= q
    for i in range(1, len(string_1) - len(string_2) + 1):
        Hash_n = ((Hash % q - ord(string_1[i - 1]) * Hash_t % q) * p % q + ord(string_1[i + len(string_2) - 1])) % q
        if Hash_n == Hash_s:
            return i
        Hash = Hash_n

    return -1
def task_2():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['a','b']))  # input
    >>> task_2()
    -1
    >>> sys.stdin = io.StringIO(chr(10).join(['zabcd','abcdz']))  # input
    >>> task_2()
    4
    """
    string_1 = input()
    string_2 = input()
    q = 2 ** 31 - 1
    print(String_1_2(string_1, string_2, q))
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)