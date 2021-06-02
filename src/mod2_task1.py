N=int(input(" "))
a= [int(i)for i in input().split(" ")]
num_swap=0
for i in range(N-1):
    for j in range(N-1-i):
        if a[j+1]<a[j]:
            t = a[j+1]
            a[j+1] = a[j]
            a[j] = t
            num_swap= num_swap+1
            for i in range(N):
                print(a[i],end=" ")
            print()
if num_swap==0:
    print(0)