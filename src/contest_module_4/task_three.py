length = int(input())
kek = list(map(int,input().split()))
my_list = [0]*length
n = 1
for i in range(length-1):
    for j in range(n, length):
        if kek[i] > kek[j]:
            my_list[i] = j
            break
    n+=1
for i in range(0,length):
    if (my_list[i] == 0):
        my_list[i] = -1
print(' '.join(map(str, my_list)))
# TL ,но работает верно 