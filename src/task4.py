input()

lst = list(map(int, input().split()))

input()

processing = Counter(map(int, input().split()))

[print('yes' if lst[i - 1] - processing[i] < 0 else 'no') for i in range(1, len(lst) + 1)]

