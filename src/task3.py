def merger(mas, List):
    new_list = [] 
    i, j = 0, 0
    while i < len(mas) and j < len(List):
        if mas[i] < List[j]:
            new_list.append(mas[i])
            i += 1
        else:
            new_list.append(List[j])
            j += 1
    while i < len(mas):   
        new_list.append(mas[i])
        i += 1
    while j < len(List):
        new_list.append(List[j])
        j += 1

    return new_list 
def merger_sort(mas, index):
    if len(mas) < 2:
        return mas
    else:
        mid = len(mas)//2
        left = merger_sort(mas[:mid], [index[0],index[0]+mid])
        right = merger_sort(mas[mid:],[index[0]+mid, index[1]]) 

        sort = merger(left, right)
        print(index[0]+1, index[1], sort[0], sort[-1])  
        return sort
Size = int(input())
mas = list(map(int, input().split())) 

mas = merger_sort(mas,[0, Size])
print(" ".join(map(str, mas)))
