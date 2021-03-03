def merge(Arr, List):
    new_list = [] 
    i, j = 0, 0
    while i < len(Arr) and j < len(List):
        if Arr[i] < List[j]:
            new_list.append(Arr[i])
            i += 1
        else:
            new_list.append(List[j])
            j += 1
    while i < len(Arr):   
        new_list.append(Arr[i])
        i += 1
    while j < len(List):
        new_list.append(List[j])
        j += 1
 
    return new_list 
 
def mergeSort(Arr, index):
    if len(Arr) < 2:
        return Arr
    else:
        mid = len(Arr)//2
        left = mergeSort(Arr[:mid], [index[0],index[0]+mid])
        right = mergeSort(Arr[mid:],[index[0]+mid, index[1]]) 
 
        sort = merge(left, right)
        print(index[0]+1, index[1], sort[0], sort[-1])  
        return sort

       
Quantity = int(input())
Arr = list(map(int, input().split())) 

Arr = mergeSort(Arr,[0, Quantity])
print(' '.join(map(str, Arr)))