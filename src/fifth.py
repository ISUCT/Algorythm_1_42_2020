n = int(input())
m = list(map(int, input().split(" ")))
sort ={}
for i in m:
    if i not in sort:
            sort[i] = 1
        
print(len(sort))
