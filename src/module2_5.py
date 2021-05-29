d = 1
m = int(input())
numbers = list(map(int, input().split(maxsplit = m)))
numbers.sort()
for c in range(1, m):
    if numbers[c-1] != numbers[c]:
        d= d+1
print(d)