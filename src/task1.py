n = int(input())
str_num = input()
str_num = str_num.split(" ")
arr=[]
for item in str_num:
	arr.append(int(item))
a = len(arr)
s = 0
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            s+=1
            print(" ".join(map(str,arr)))
if s==0:
    print(0)