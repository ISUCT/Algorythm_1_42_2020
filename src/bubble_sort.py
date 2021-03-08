n= int(input())
arr = input()
str_lst = arr.split()
res = []
num = True
for item in str_lst:
    res.append(int(item))
   
n = len(res)
for i in range (0, n-1):
    #print(i)
    for j in range(0, n-i-1):
        #print(j)
        if res[j] > res[j+1]:
            num = False
            res[j],res[j+1] = res[j+1],res[j]
            print(" ".join(map(str, res)))

if num == True:
    print(0)