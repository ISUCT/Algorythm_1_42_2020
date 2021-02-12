inp = input()
splt = inp.split(" ")
print(splt)
res = []
for item in splt:
    res.append(int(item))
print(res[0]+res[1])