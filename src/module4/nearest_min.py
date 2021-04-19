def find_index_of_mininal(items):
    stack = []
    result = []

    for i in range(len(items)):
        item = items[i]

        if len(stack) > 0 and (item < stack[-1][1]):
            result.insert(stack[-1][0], i)
            stack.pop()

        stack.append((i, item));

    for i in range(len(stack) - 1):
        item = stack[i]
        result.insert(item[0], stack[i + 1][0] if stack[i + 1][1] < item[1] else -1)

    return result + [-1]

def get_input_data():
    length = int(input())
    items = list(map(int, input().split()))

    return items, length


def main():
    '''
    <<< 10
    <<< 1 2 3 2 1 4 2 5 3 1
    >>> main()
    -1 4 3 4 -1 6 9 8 9 -1
    '''
    items, length = get_input_data()
    result = find_index_of_mininal(items)

    print(*result, sep=' ')


if __name__ == '__main__':
    main()