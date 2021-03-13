def sorting():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['4','4 3 2 1']))  # input
    >>> sorting()
    3 4 2 1
    3 2 4 1
    3 2 1 4
    2 3 1 4
    2 1 3 4
    1 2 3 4
    """
    n = int(input())
    str_numbers = input()
    str_lst = str_numbers.split(" ")
    num = []
    for item in str_lst:
        num.append(int(item))

    count = 0
    for i in range(len(num)-1):
        for j in range(len(num)-1-i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                count += 1
                print(" ".join(map(str,num)))
    if count == 0:
        print(count)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)