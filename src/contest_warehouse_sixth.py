Quantity_products = int(input())
Products = list(map(int, input().split()))

Quantily_order = int(input())
Order = list(map(int,input().split()))

Count = [0] * (Quantity_products+1) 
for now in Order:
    Count[now] += 1

for i in range(Quantity_products):
    if Products[i] < Count[i+1]:
        print("yes")
    else:
        print("no")