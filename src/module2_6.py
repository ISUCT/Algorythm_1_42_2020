quantity_product = int(input())
product = list(map(int, input().split()))

quantily_purpose = int(input())
purpose = list(map(int,input().split()))

calculate = [0] * (quantity_product+1) 
for now in purpose:
    calculate[now] += 1

for i in range(quantity_product):
    if product[i] < calculate[i+1]:
        print("yes")
    else:
        print("no") 