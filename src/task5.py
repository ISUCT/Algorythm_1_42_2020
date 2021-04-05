number = int(input())
array = list(map(int,input().split(" ")))
res = {}
for item in array:
    res[item] = 1
print(len(res))


