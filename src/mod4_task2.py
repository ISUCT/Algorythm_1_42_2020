p = int(input())
c = list(map(int, input().split()))

impasse = [0] 
wayB = [0] 

for i in range(p):
    while impasse[-1] == wayB[-1] + 1:
       wayB.append(impasse[-1])
       impasse.pop()
    if c[i] == wayB[-1] + 1:
        wayB.append(c[i])
    else:
        impasse.append(c[i])

while impasse[-1] == wayB[-1] + 1:
    wayB.append(impasse[-1])
    impasse.pop()

if wayB[-1] == p:
    print('YES')
else:
    print('NO')