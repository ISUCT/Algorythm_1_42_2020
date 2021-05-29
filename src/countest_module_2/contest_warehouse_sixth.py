Quantity_products = int(input())
Products = list(map(int, input().split()))

order = int(input())
O = list(map(int,input().split()))

C = [0] * (Quantity_products+1) 
for now in Order:
    C[now] += 1

for i in range(Quantity_products):
    if Products[i] < C[i+1]:
        print("yes")
    else:
        print("no")