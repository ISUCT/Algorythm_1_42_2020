def merge(A, List):
    new_list = [] 
    i, j = 0, 0
    while i < len(A) and j < len(List):
        if A[i] < List[j]:
            new_list.append(A[i])
            i += 1
        else:
            new_list.append(List[j])
            j += 1
    while i < len(A):   
        new_list.append(A[i])
        i += 1
    while j < len(List):
        new_list.append(List[j])
        j += 1
 
    return new_list 
 
def mergeSort(A, index):
    if len(A) < 2:
        return A
    else:
        mid = len(A)//2
        left = mergeSort(A[:mid], [index[0],index[0]+mid])
        right = mergeSort(A[mid:],[index[0]+mid, index[1]]) 
 
        so = merge(left, right)
        print(index[0]+1, index[1], s[0], s[-1])  
        return s

       
q = int(input())
A = list(map(int, input().split())) 

A = mergeSort(A,[0, q])
print(' '.join(map(str, A)))