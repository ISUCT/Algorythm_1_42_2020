# TL on Yandex.Contest
def get_shift_size(first_string, second_string):
    if first_string == second_string:
        return 0

    result = -1

    offset = 0
    length = len(first_string)

    while (length - offset) > 0:
        prefix = first_string[offset:length]
        suffix = second_string[:length - offset]

        if prefix == suffix:
            result = length - offset
            break

        offset += 1

    return result


def get_input_data():
    first_string = input()
    second_string = input()

    return first_string, second_string


def main():
    '''
    <<< abc
    <<< abc
    >>> main()
    0

    <<< a
    <<< b
    >>> main()
    -1

    <<< zabcd
    <<< abcdz
    >>> main()
    4
    '''
    first_string, second_string = get_input_data()

    result = get_shift_size(first_string, second_string)
    print(result)


if __name__ == '__main__':
    main()
