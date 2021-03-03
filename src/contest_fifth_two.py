# new_list = []
# Quantity = int(input())
# Arr = list(map(int,input().split(" ")))
# for i in range(0,Quantity):
#   if Arr[i] not in new_list:
#     new_list.append(Arr[i])
# Result=len(new_list)
# print(Result)


Quantity = int(input())
Arr = list(map(int,input().split(" ")))
new_list = {}
 
for i in Arr:
	if i not in new_list:
		new_list[i] = 1
 
print(len(new_list))