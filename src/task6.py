tore = int(input())
products = list(map(int,input().split(" ")))
order_num = int(input())
order = list(map(int,input().split(" ")))
temp = [0]*(store+1)
for item in order:
    temp[item] += 1
for i in range(store):
    if products[i] >= temp[i+1]:
        print("no")
    else:
        print("yes")