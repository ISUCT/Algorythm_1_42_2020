def number_of_different(array):
    count = 0

    max_item = max(array)
    min_item = min(array)

    counters = [0] * (max_item - min_item + 1)

    for item in array:
        counters[item - min_item] += 1

    for counter in counters:
        count += 1 if counter > 0 else 0

    return count


def get_input_data():
    length = int(input())
    array = list(map(int, input().split()))

    return array, length


def main():
    '''
    <<< 5
    <<< 1 0 1 2 0
    >>> main()
    3

    <<< 39
    <<< 2  3  8  7  1  2  2  2  7  3  9  8  2  1  4  2  4  6  9  2
    >>> main()
    8

    <<< 1
    <<< -1
    >>> main()
    1

    <<< 2
    <<< -1 -2
    >>> main()
    2
    '''
    array, length = get_input_data()
    count = number_of_different(array)

    print(count)


if __name__ == '__main__':
    main()
