input()
m = [int(i) for i in input().split(" ")]
input()
m1 = [int(i) for i in input().split(" ")]
for i in range(len(m)):
    if m1.count(i+1)>m[i]:
        print("yes")
    else:
        print("no")