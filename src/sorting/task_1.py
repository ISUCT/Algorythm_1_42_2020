n=int(input())
arr=""
arr=input()
res=arr.split(" ")
res=list(map(int,res))

num_swap=True
for i in range(0,n):
 for j in range(0,n-i-1):
     if res[j]>res[j+1]:
         res[j],res[j+1]=res[j+1],res[j]
         num_swap=False
         print(" ".join(map(str,res)))
if num_swap:
    print(0)