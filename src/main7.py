b = {}
s = int(input())
n = input()
s = n.split()
for i in s:
    b[int(i)] = 1
print(len(b))
