def merge(Arr, List):
    new_list = [] 
    d, m = 0, 0
    while d < len(Arr) and m < len(List):
        if Arr[d] < List[m]:
            new_list.append(Arr[d])
            d += 1
        else:
            new_list.append(List[m])
            m += 1
    while d < len(Arr):   
        new_list.append(Arr[d])
        d += 1
    while m < len(List):
        new_list.append(List[m])
        m += 1

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