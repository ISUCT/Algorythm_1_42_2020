def invers_fun(num):
    n = len(num)
    if n <= 1:
        return num, 0
    mid = n//2
    left, left_inv = invers_fun(num[:mid])    
    right, right_inv = invers_fun(num[mid:])
    cout, s = sort(left, right)
    m = s + left_inv + right_inv
    return cout, m

def sort(left, right):
    s = 0
    cout = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            cout.append(left[i])
            i += 1
        else:
            cout.append(right[j])
            j += 1
            s += len(left) - i
    while i < len(left):
        cout.append(left[i])
        i += 1
    while j < len(right):
        cout.append(right[j])
        j += 1
    return cout, s    

n = int(input())
num = list(map(int, input().split(" ")))
num, inversions = invers_fun(num)
print(inversions)