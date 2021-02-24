# Проходит стандартные тесты, но на Яндекс.Контест проваливает 8-й тест
def number_of_different_old(array):
    length = -1
    count = 0

    for item in array:
        if item > length:
            length = item

    counters = [0] * (length + 1)
    output = [0] * len(array)

    for item in array:
        counters[item] += 1

    for counter in counters:
        if counter > 0:
            count += 1

    return count


def number_of_different(array):
    return len(set(array))


def get_input_data():
    length = int(input())
    array = list(map(int, input().split()))

    return array, length


def main():
    '''
    <<< 5
    <<< 1 0 1 2 0
    >>> main()
    3

    <<< 39
    <<< 2  3  8  7  1  2  2  2  7  3  9  8  2  1  4  2  4  6  9  2
    >>> main()
    8
    '''
    array, length = get_input_data()
    count = number_of_different(array)

    print(count)


if __name__ == '__main__':
    main()
