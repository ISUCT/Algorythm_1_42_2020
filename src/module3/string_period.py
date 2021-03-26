def find_prefixes(string):
    length = len(string)
    prefixes = [0] * length

    for i in range(length - 1):
        j = prefixes[i]

        while (j > 0) and (string[i + 1] != string[j]):
            j = prefixes[j - 1]

        if string[i + 1] == string[j]:
            prefixes[i + 1] = j + 1
        else:
            prefixes[i + 1] = 0

    return prefixes


def find_period(string):
    prefixes = find_prefixes(string)

    length = len(string)
    result = length - prefixes[length - 1]

    if length % result == 0:
        return length // result

    return 1


def get_input_data():
    return input()


def main():
    '''
    <<< aaaaa
    >>> main()
    5

    <<< abcabcabc
    >>> main()
    3

    <<< abab
    >>> main()
    2
    '''
    string = get_input_data()
    result = find_period(string)

    print(result)


if __name__ == '__main__':
    main()
