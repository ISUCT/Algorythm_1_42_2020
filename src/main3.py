def sort (a , n):
    for i in range(0 , n):
    for j in range(0 , n-i-1):
        if a[j] > a[j + 1]:
            a[j + 1] , a[j] = a[j] , a[j + 1]2



n = "4" #input()
inp = "4 3 2 1"
lst = inp.split(" ")
res = []
for i in range (0 , n):
    res.append(int(lst[i]))

print(res)