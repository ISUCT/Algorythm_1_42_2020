k = int(input())
B = [0]*k
for i in range(k):
    B[i] = list(map(int, input().split()))
B.sort(key=lambda x: x[0])
B.sort(key=lambda x: x[1],reverse=1)
for i in range(k):
    print(B[i][0], B[i][1])