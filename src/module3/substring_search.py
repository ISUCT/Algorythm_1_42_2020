def hash(string, x, p):
    '''
    >>> hash('abc', 26, 1e9+7) == hash('abc', 26, 1e9+7)
    True
    >>> hash('abc', 26, 1e9+7) == hash('bca', 26, 1e9+7)
    False
    >>> hash('', 26, 1e9+7) == hash('', 26, 1e9+7)
    True
    '''
    result = 0

    for i in range(len(string)):
        result = (result * x + ord(string[i])) % p

    return result


# Если есть % p, то выдает RE, иначе TL :(
def find_occurences(string, substring):
    string_length = len(string)
    substring_length = len(substring)

    if string_length < substring_length:
        return []

    x = 26
    p = 1e9 + 7

    string_hash = hash(string[:substring_length], x, p)
    substring_hash = hash(substring, x, p)

    occurences = []

    for i in range(string_length - substring_length + 1):
        if (substring_hash == string_hash) and (substring == string[i:i + substring_length]):
            occurences.append(i)

        if (i + substring_length) < string_length:
            string_hash *= x
            string_hash -= ord(string[i]) * pow(x, substring_length)
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
