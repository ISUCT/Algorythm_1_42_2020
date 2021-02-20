n = int(input())
arr = []
num = []
for i in range(0 , n):
    arr = input().split(" ")
    for item in arr:
        num.append(int(item))
for j in range(0, n):
    for i in range(0, n):
        if num[i+1] > num[i+3]:
            num[i + 1],num[i + 3] = num[i + 3],num[i + 1]
            num[i],num[i + 2] = num[i + 2],num[i]
        if num[i+1] == num[i+3]:
            if num[i] > num[i+2]:
                num[i + 1],num[i + 3] = num[i + 3],num[i + 1]
                num[i],num[i + 2] = num[i + 2],num[i]
new_items = ['{} {}'.format(num[i], num[i + 1]) for i in range(0, len(num), 2)]
for i in range(0 , n):
    print(new_items[i])
    