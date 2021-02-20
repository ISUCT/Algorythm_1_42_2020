n = int(input())
arr = []
num = []
for i in range(0 , n):
    arr = input().split(" ")
    num.append([])
    for item in arr:
        num[i].append(int(item))
print(arr)
for j in range(n):
    for i in range(n-1):
        if(num[i][1] < num[i+1][1]):
            num[i][0],num[i+1][0] = num[i+1][0],num[i][0]
            num[i][1],num[i+1][1] = num[i+1][1],num[i][1]
        if(num[i][1] == num[i+1][1]):
            if(num[i][0] > num[i+1][0]):
                num[i][0],num[i+1][0] = num[i+1][0],num[i][0]
                num[i][1],num[i+1][1] = num[i+1][1],num[i][1]
for i in range(n):    
    print(str(num[i][0]) + " " + str(num[i][1]))