s = input()
t = input()
res = []
for i in range(len(t), len(s)+1):
    if t == s[i-len(t):i]:
        res.append(i-len(t))
print(" ".join(map(str,res)))