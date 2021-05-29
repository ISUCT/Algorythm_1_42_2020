one = str(input())
two = str(input())
str_one = list(one)
str_two = list(two)
Count = 0 
for i in range(len(str_one)-1,-1,-1):
    if str_one != str_two:
        str_one.insert(0, str_one.pop())
        Count+=1
if str_one != str_two:
    Count = -1
print(Count)