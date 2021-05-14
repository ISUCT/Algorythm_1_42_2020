"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join([\
'1',\
'1'\
]))
>>> task_merge_sort()
1
>>> sys.stdin = io.StringIO(chr(10).join([\
'2',\
'3 1',\
]))
>>> task_merge_sort()
1 2 1 3
1 3 
>>> sys.stdin = io.StringIO(chr(10).join([\
'5',\
'5 4 3 2 1',\
]))
>>> task_merge_sort()
1 2 4 5
4 5 1 2
3 5 1 3
1 5 1 5
1 2 3 4 5 
>>> print(merge([2,3,4],[1,2,3]))
[1, 2, 2, 3, 3, 4]
"""

def merge(A, B):
    res = []
    i = 0
    j = 0
    for k in range(0, len(A)+len(B)):
        if j == len(B) or A[i] < B[j]:
            res.append(A[i])
            i +=1
        else:
            res.append(B[j])
            j += 1
    return res

def merge_sort(A):
    if len(A) == 1:
        return A
    l = A[0:len(A)//2]
    r = A[len(A)//2:]
    l = merge_sort(l)
    r = merge_sort(r)
    print("{:d} {:d}".format(r[0], l[-1]))
    return merge(l, r)

def task_merge_sort():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    res = merge_sort(arr)
    print(" ".join(list(map(str,res))))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)