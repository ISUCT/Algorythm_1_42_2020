def get_shift_size(first_string, second_string):
    if second_string == first_string:
        return 0

    second_string *= 2

    p = 13
    m = 1
    q = 2**31 - 1

    first_hash = 0
    second_hash = 0
    xt = 1

    for i in first_string[::-1]:
        first_hash = (first_hash + ord(i) * m) % q
        m = (m * p) % q

    m = 1
    for i in second_string[:len(first_string)][::-1]:
        second_hash = (second_hash + ord(i) * m) % q
        m = (m * p) % q

    for i in range(len(first_string) - 1):
        xt = (xt * p) % q

    for i in range(1, len(second_string) - len(first_string) + 1):
        if second_hash == first_hash:
            return i - 1

        second_hash = p * (second_hash - ord(second_string[i - 1]) * xt)
        second_hash += ord(second_string[i + len(first_string) - 1])
        second_hash %= q

    return -1


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
