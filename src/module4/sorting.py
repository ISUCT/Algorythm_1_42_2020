def can_be_sorted(wagons):
    stack = []
    result = []

    length = len(wagons)
    sorted_wagons = sorted(wagons)

    while len(result) < length:
        if len(wagons) > 0 and len(stack) == 0:
            stack.append(wagons.pop(0))
            continue

        if len(wagons) > 0 and wagons[0] <= stack[-1]:
            stack.append(wagons.pop(0))
        else:
            result.append(stack.pop())

    return result == sorted_wagons


def get_input_data():
    length = int(input())
    wagons = list(map(int, input().split()))

    return wagons, length


def main():
    '''
    <<< 3
    <<< 3 2 1
    >>> main()
    YES

    <<< 4
    <<< 4 1 2 3
    >>> main()
    YES

    <<< 3
    <<< 2 3 1
    >>> main()
    NO
    '''
    wagons, length = get_input_data()
    result = can_be_sorted(wagons)

    print('YES' if result else 'NO')


if __name__ == '__main__':
    main()
