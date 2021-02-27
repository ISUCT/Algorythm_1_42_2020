n=int(input(" "))
arr= [int(i)for i in input().split(" ")]
c=0
for i in range(n-1):
    for j in range(n-1):
        if arr[j+1]<arr[j]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            c+=1
            for i in range(n):
                print(arr[i],end=" ")
            print()
if c==0:
    print(0)

