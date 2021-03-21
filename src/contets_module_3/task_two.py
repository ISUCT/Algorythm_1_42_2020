one = str(input())
two = str(input())
string_one = list(one)
string_two = list(two)
Counter = 0 
for i in range(len(string_one)-1,-1,-1):
    if string_one != string_two:
        string_one.insert(0, string_one.pop())
        Counter+=1
if string_one != string_two:
    Counter = -1
print(Counter)