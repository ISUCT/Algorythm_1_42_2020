def merge(left_array, right_array):
    result = []
    inversions = 0
    i = j = 0

    while i < len(left_array) and j < len(right_array):
        left, right = left_array[i], right_array[j]

        if left <= right:
            result.append(left)
            i += 1
        else:
            result.append(right)
            inversions += len(left_array) - i
            j += 1

    result += left_array[i:]
    result += right_array[j:]

    return result, inversions


def merge_sort(array):
    if len(array) <= 1:
        return array, 0

    middle_index = len(array) // 2

    left_array, left_inversions = merge_sort(array[:middle_index])
    right_array, right_inversions = merge_sort(array[middle_index:])

    result, inversions = merge(left_array, right_array)

    return result, left_inversions + inversions + right_inversions


def get_input_data():
    length = int(input())
    array = list(map(int, input().split()))

    return array, length


def main():
    '''
    <<< 1
    <<< 1
    >>> main()
    0

    <<< 2
    <<< 3 1
    >>> main()
    1

    <<< 5
    <<< 5 4 3 2 1
    >>> main()
    10
    '''
    array, length = get_input_data()

    result, inversions = merge_sort(array)
    print(inversions)


if __name__ == '__main__':
    main()
