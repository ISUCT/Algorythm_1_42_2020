c = 1
n = int(input())
numbers = list(map(int, input().split(maxsplit = n)))
numbers.sort()
for i in range(1, n):
    if numbers[i-1] != numbers[i]:
        c= c+1
print(c)