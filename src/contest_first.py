Quantity = int(input())
Arr = list(map(int,input().split(" ")))
Counter = 0
for i in range(Quantity-1):
   for j in range(Quantity-i-1):
        if Arr[j] > Arr[j+1]:
            Arr[j], Arr[j+1] = Arr[j+1], Arr[j]
            Counter += 1
            print(' '.join(map(str, Arr)))
if Counter == 0:
    print(Counter)