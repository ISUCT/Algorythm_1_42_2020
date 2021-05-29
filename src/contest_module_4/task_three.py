l = int(input())
k = list(map(int,input().split()))
my_list = [0]*l
n = 1
for i in range(l-1):
    for j in range(n, l):
        if k[i] > k[j]:
            my_list[i] = j
            break
    n+=1
for i in range(0,l):
    if (my_list[i] == 0):
        my_list[i] = -1
print(' '.join(map(str, my_list)))
