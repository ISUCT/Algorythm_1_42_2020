def sorting():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['3','101 80','305 90', '200 14']))  # input
    >>> sorting()
    305 90
    101 80
    200 14
    """
    """
    >>> sys.stdin = io.StringIO(chr(10).join(['3','20 80','30 90', '25 90']))  # input
    >>> sorting()
    25 90
    30 90
    20 80
    """
    N = int(input())
    id_nums = []
    for i in range(N):
        str_numbers = input().split(" ")
        id_nums.append(str_numbers)
        for j in range(len(id_nums[i])):
            id_nums[i][j] = int(id_nums[i][j])
    for i in range(len(id_nums) - 1):
        for j in range(len(id_nums) - i - 1):
            item = id_nums[j]
            next_it = id_nums[j + 1]
            if (item[1] < next_it[1]) or (item[1] == next_it[1] and item[0] >= next_it[0]):
                id_nums[j], id_nums[j + 1] = next_it, item
    for i in range(len(id_nums)):
        print(" ".join(map(str, id_nums[i])))
sorting()
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
