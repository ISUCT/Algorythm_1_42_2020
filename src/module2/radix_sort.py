def sorting_phase(array, index):
    sorted_array = ['0'] * len(array)
    buckets = [[] for i in range(10)]

    for item in array:
        buckets[int(item[index])].append(item)

    for i in range(10):
        print(f'Bucket {i}: ', end='')
        print(', '.join(buckets[i]) if len(buckets[i]) > 0 else 'empty')

    p = 0
    for i in range(10):
        for item in buckets[i]:
            sorted_array[p] = item
            p += 1

    return sorted_array


def radix_sort(array):
    phases = len(array[0])
    sorted_array = array

    for phase in range(1, phases + 1):
        print('**********')
        print(f'Phase {phase}')

        sorted_array = sorting_phase(sorted_array, -1 * phase)

    print('**********')

    return sorted_array


def get_input_data():
    array = []
    length = int(input())

    for i in range(length):
        array.append(input())

    return array, length


def main():
    '''
    <<< 9
    <<< 12
    <<< 32
    <<< 45
    <<< 67
    <<< 98
    <<< 29
    <<< 61
    <<< 35
    <<< 09
    >>> main()
    Initial array:
    12, 32, 45, 67, 98, 29, 61, 35, 09
    **********
    Phase 1
    Bucket 0: empty
    Bucket 1: 61
    Bucket 2: 12, 32
    Bucket 3: empty
    Bucket 4: empty
    Bucket 5: 45, 35
    Bucket 6: empty
    Bucket 7: 67
    Bucket 8: 98
    Bucket 9: 29, 09
    **********
    Phase 2
    Bucket 0: 09
    Bucket 1: 12
    Bucket 2: 29
    Bucket 3: 32, 35
    Bucket 4: 45
    Bucket 5: empty
    Bucket 6: 61, 67
    Bucket 7: empty
    Bucket 8: empty
    Bucket 9: 98
    **********
    Sorted array:
    09, 12, 29, 32, 35, 45, 61, 67, 98
    '''
    array, length = get_input_data()

    print('Initial array:')
    print(', '.join(array))

    sorted_array = radix_sort(array)

    print('Sorted array:')
    print(', '.join(sorted_array))


if __name__ == '__main__':
    main()
