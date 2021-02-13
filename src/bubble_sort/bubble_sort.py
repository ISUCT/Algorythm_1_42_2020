def bubble_sort(array):
    length = len(array)
    swapped = False

    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                print(' '.join(map(str, array)))

    if not swapped:
        print(0)


def main():
    length = int(input())
    array = list(map(int, input().split()))

    result = bubble_sort(array)
    print(" ".join(map(str, result)))


if __name__ == '__main__':
    main()
