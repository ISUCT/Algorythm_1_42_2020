def read_item():
    return list(map(int, input().split()))


def pairs_sort(items, length):
    item = read_item()
    items.append(item)

    for i in range(1, length):
        item = read_item()
        items.append(item)

        j = i

        while (j > 0) and ((items[j - 1][1] < item[1]) or (items[j - 1][1] == item[1] and items[j - 1][0] > item[0])):
            items[j] = items[j - 1]
            j -= 1

        items[j] = item


def main():
    '''
    <<< 3
    <<< 101 80
    <<< 305 90
    <<< 200 14
    >>> main()
    305 90
    101 80
    200 14

    <<< 3
    <<< 20 80
    <<< 30 90
    <<< 25 90
    >>> main()
    25 90
    30 90
    20 80

    <<< 3
    <<< 20 90
    <<< 20 90
    <<< 20 90
    >>> main()
    20 90
    20 90
    20 90
    '''
    length = int(input())
    items = []

    pairs_sort(items, length)

    for item in items:
        print(*item, sep=' ')


if __name__ == '__main__':
    main()
