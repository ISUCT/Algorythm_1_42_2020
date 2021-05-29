l = int(input())
tr_a = list(map(int,input().split()))
tr_b = []
t = []
test =  sorted(tr_a)
for i in range(l):
    if (t == []) or (t[-1] > tr_a[0]):
        t.append(tr_a[0])
        tr_a.pop(0)
    else:
        while (t != [] and t[-1] < tr_a[0]):
            tr_b.append(t[-1])
            t.pop(-1)
        if (t == []) or (t[-1] > tr_a[0]):
            t.append(tr_a[0])
            tr_a.pop(0)        
if t != []: 
    for i in range(len(t)):
        tr_b.append(t[-1])
        t.pop(-1)   
if tr_b == test:
    print("YES")
else: 
    print("NO")