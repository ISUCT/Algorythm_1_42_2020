def merge_sort(num, start,end):
    if (end - start > 1):
        mid = (start + end) // 2
        merge_sort(num, start, mid)
        merge_sort(num, mid, end)
        left = num [start: mid]
        right = num[mid: end]
        internal_sort(num, left, right, start)
        print(start +1, end, num[start], num[end - 1])
def internal_sort(mass, left, right, start):
    i = j = 0 # i -> right j -> left
    k = start
    while i < len(right) and j < len(left):
        if left[j] > right[i]:
            mass[k] = right[i]
            i = i+1
        else:
            mass[k] = left[j]
            j =j+1
        k =k+1
    while j < len(left):
        mass [k] = left[j]
        j=j+1
        k=k+1
    while i < len(right):
        mass[k] = right[i]
        i=i+1
        k=k+1        
def main():
    n = int(input())
    num = list(map(int, input().split(maxsplit = n)))
    merge_sort(num, 0, len(num))
    print(*num)
    
main() 