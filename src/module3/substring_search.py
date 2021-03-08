def find_occurences(string, substring):
    string_length = len(string)
    substring_length = len(substring)

    if string_length < substring_length:
        return []

    occurences = []

    x = 26
    p = 101

    string_hash = 0
    substring_hash = 0

    xt = 1

    for i in range(substring_length - 1):
        xt = (xt * x) % p

    for i in range(substring_length):
        string_hash = (string_hash * x + ord(string[i])) % p
        substring_hash = (substring_hash * x + ord(substring[i])) % p

    for i in range(string_length - substring_length + 1):
        if (substring_hash == string_hash) and (substring == string[i:i+substring_length]):
            occurences.append(i)

        if (i + substring_length) < string_length:
            string_hash = x * (string_hash - ord(string[i]) * xt)
            string_hash += ord(string[i + substring_length])
            string_hash %= p

    return occurences


def get_input_data():
    string = input()
    substring = input()

    return string, substring


def main():
    '''
    <<< ababbababa
    <<< aba
    >>> main()
    0 5 7
    '''
    string, substring = get_input_data()
    occurences = find_occurences(string, substring)

    print(*occurences, sep=' ')


if __name__ == '__main__':
    main()
