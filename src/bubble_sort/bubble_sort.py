def bubble_sort(array, on_shuffle=None):
    length = len(array)

    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def bubble_sort_shuffles(array):
    length = len(array)
    shuffles = 0

    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                shuffles += 1

    return shuffles


def main():
    length = int(input())
    array = list(map(int, input().split()))

    result = bubble_sort(array)
    print(" ".join(map(str, result)))

    shuffles = bubble_sort_shuffles(array)
    print(shuffles)


if __name__ == '__main__':
    main()
