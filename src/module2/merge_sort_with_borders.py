def merge(left_array, right_array, left_index, right_index):
    result = []
    i = j = 0

    while i < len(left_array) and j < len(right_array):
        left, right = left_array[i], right_array[j]

        if left < right:
            result.append(left)
            i += 1
        else:
            result.append(right)
            j += 1

    result += left_array[i:]
    result += right_array[j:]

    print(
        f'{left_index + 1} {right_index + 1} {result[0]} {result[-1]}')

    return result


def merge_sort(array, left_index, right_index):
    if len(array) <= 1:
        return array

    middle_index = len(array) // 2

    left_array = merge_sort(
        array[:middle_index], left_index, left_index + middle_index - 1)
    right_array = merge_sort(
        array[middle_index:], left_index + middle_index, right_index)

    return merge(left_array, right_array, left_index, right_index)


def get_input_data():
    length = int(input())
    array = list(map(int, input().split()))

    return array, length


def main():
    '''
    <<< 2
    <<< 3 1
    >>> main()
    1 2 1 3
    1 3

    <<< 5
    <<< 5 4 3 2 1
    >>> main()
    1 2 4 5
    4 5 1 2
    3 5 1 3
    1 5 1 5
    1 2 3 4 5
    '''
    array, length = get_input_data()

    result = merge_sort(array, 0, length - 1)
    print(*result, sep=' ')


if __name__ == '__main__':
    main()
