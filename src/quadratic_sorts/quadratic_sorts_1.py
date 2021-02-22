def sort_by_cost_and_id(items):
    length = len(items)

    for i in range(length - 1):
        for j in range(length - i - 1):
            item = items[j]
            next_item = items[j + 1]

            if (item[1] < next_item[1]) or (item[1] == next_item[1] and item[0] >= next_item[0]):
                items[j], items[j + 1] = next_item, item

    for item in items:
        print(' '.join(map(str, item)))


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
    '''
    items = []
    length = int(input())

    for i in range(length):
        item = list(map(int, input().split()))
        items.append(item)

    sort_by_cost_and_id(items)


if __name__ == '__main__':
    main()
