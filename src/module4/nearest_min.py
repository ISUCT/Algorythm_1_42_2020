def find_index_of_mininal(items):
    stack = []
    result = [0] * len(items)

    for i in range(len(items) - 1, -1, -1):
        while stack and (items[stack[-1]] >= items[i]):
            stack.pop()

        result[i] = stack[-1] if stack else -1
        stack.append(i)

    return result

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