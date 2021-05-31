n = int(input())
arr = input()
lst = arr.split(' ')
res = []
s = True
for item in lst:
    res.append(int(item))
n = len(res)
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if res[j] > res[j+1]:
            s = False
            temp = res[j+1]
            res[j+1] = res[j]
            res[j] = temp
            print(" ".join(map(str, res)))

if s == True:
    print(0)
