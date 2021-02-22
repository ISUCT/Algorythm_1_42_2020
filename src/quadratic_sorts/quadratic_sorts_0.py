def bubble_sort(array):
    length = len(array)
    swapped = False

    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                print(' '.join(map(str, array)))

    if not swapped:
        print(0)


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
    length = int(input())
    array = list(map(int, input().split()))

    bubble_sort(array)


if __name__ == '__main__':
    main()
