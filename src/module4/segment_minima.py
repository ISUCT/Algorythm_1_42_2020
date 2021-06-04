def find_minimums(items, n, k):
    deque = []
    result = []

    for i in range(k):
        while deque and (items[i] < items[deque[-1]]):
            deque.pop()

        deque.append(i)

    result.append(items[deque[0]])

    for i in range(k, n):
        while deque and (deque[0] <= i - k):
            deque.pop(0)

        while deque and (items[i] < items[deque[-1]]):
            deque.pop()

        deque.append(i)
        result.append(items[deque[0]])

    return result


def get_input_data():
    n, k = list(map(int, input().split()))
    items = list(map(int, input().split()))

    return items, n, k


def main():
    '''
    <<< 7 3
    <<< 1 3 2 4 5 3 1
    >>> main()
    1
    2
    2
    3
    1
    '''
    items, n, k = get_input_data()
    result = find_minimums(items, n, k)

    print(*result, sep='\n')


if __name__ == '__main__':
    main()