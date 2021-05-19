n=int(input())
s=list(map(int, input (). split()))
massiv=[]
bool_var= True
number=1
for i in s:
    for _ in range (len(massiv)):
        if massiv and number == massiv[-1]:
            massiv.pop()
            number+=1
    if i!=number:
        if massiv and i>massiv[-1]:
            bool_var= False
            break
        massiv.append(i)
    else:
        number+=1
if bool_var:
    print ("YES")
else:
    print ("NO")