def sort_process(array, length):
    swapped = False

    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                print(*array, sep=' ')

    if not swapped:
        print(0)


def get_input_data():
    length = int(input())
    array = list(map(int, input().split()))

    return array, length


def main():
    '''
    <<< 4
    <<< 4 3 2 1
    >>> main()
    3 4 2 1
    3 2 4 1
    3 2 1 4
    2 3 1 4
    2 1 3 4
    1 2 3 4
    '''
    array, length = get_input_data()

    sort_process(array, length)


if __name__ == '__main__':
    main()
