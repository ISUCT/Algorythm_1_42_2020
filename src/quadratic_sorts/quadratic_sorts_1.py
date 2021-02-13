def main():
    items = []
    length = int(input())

    for i in range(length):
        item = list(map(int, input().split()))
        items.append(item)

    for i in range(length - 1):
        for j in range(length - i - 1):
            item = items[j]
            next_item = items[j + 1]

            if (item[1] < next_item[1]) or (item[1] == next_item[1] and item[0] >= next_item[0]):
                items[j], items[j + 1] = next_item, item

    for item in items:
        print(' '.join(map(str, item)))


if __name__ == '__main__':
    main()
