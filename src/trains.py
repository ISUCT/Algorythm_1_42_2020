l = int(input())
s = list(map(int, input().split()))
 
deadlock = [0] 
wayB = [0] 
 
for i in range(l):
    while deadlock[-1] == wayB[-1] + 1:
       wayB.append(deadlock[-1])
       deadlock.pop()
    if s[i] == wayB[-1] + 1:
        wayB.append(s[i])
    else:
        deadlock.append(s[i])
 
while deadlock[-1] == wayB[-1] + 1:
    wayB.append(deadlock[-1])
    deadlock.pop()
 
if wayB[-1] == l:
    print('YES')
else:
    print('NO')
