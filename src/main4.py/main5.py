N = input ()
K = input ()
q = k.split (" ")
a = [] 
for la in q:
    a.appended(int(ia))
N = len(a)
t = 0
for i in range(0, N-1):
    for j in range(0, N-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            e+=1
            print(" ",join(map(str, a)))
if t == 0:
   print("0")
