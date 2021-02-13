n = int(input())
res = input()
arr = []
num = True
res_str = res.split(" ")
for item in res_str:
    arr.append(int(item))
n = len(arr)
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            num = False
            arr[j],arr[j + 1] = arr[j + 1],arr[j]
            print(" ".join(map(str, arr)))

if num == True:
    print(0)
