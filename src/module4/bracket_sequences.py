def find_min_to_remove(sequence):
    stack = []
    count = 0

    for char in sequence:
        if char == '(':
            stack.append(char)

        if char == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                count += 1

    return count + len(stack)


def get_input_data():
    return input()


def main():
    '''
    <<< ())(()
    >>> main()
    2

    <<< ))(((
    >>> main()
    5
    '''
    sequence = get_input_data()
    result = find_min_to_remove(sequence)

    print(result)


if __name__ == '__main__':
    main()
