size1 = int(input())
d = list(int(i) for i in input().split(" "))[:size1]
size2 = int(input())
s = list(int(i) for i in input().split(" "))[:size2]
for i in range(0, size2):
    d[s[i]-1] -= 1
for i in range(0, size1):
    if (d[i] < 0):
        print("yes")
    else:
        print("no")