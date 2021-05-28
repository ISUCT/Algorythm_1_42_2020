N = int(input())
train = list(map(int, input().split()))
w = [0]
t = [0] 
for i in range(N):
    while t[-1] == w[-1] + 1:
        w.append(t[-1])       
        t.pop()
    if train[i] == w[-1] + 1: 
        w.append(train[i])    
    else:
        t.append(train[i])

while t[-1] == w[-1] + 1: 
    w.append(t[-1])       
    t.pop() 
if w[-1] == N: 
    print("YES") 
else:
    print("NO")