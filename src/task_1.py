#Первый вариант
inp = input()
splt = inp.split(" ")
print(splt)
res = []
for item in splt:
    res.append(int(item))
print(res[0]+res[1])

#Второй вариант
a,b = [int(item) for item in input().split(" ")]
print (a+b)