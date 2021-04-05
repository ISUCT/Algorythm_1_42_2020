#print("Hello, " + input() + "!")
def sort_insert(A):
    for n in range(1,len(A)):
        k = n
        while k>0 and A[k] < A[k-1]:
            A[k],A[k-1] = A[k-1],A[k]
            k -= 1
def sort_choice(A):
    pass
def sort_bubble(A):
    pass

def test_sort(func):
    A = [5,6,7,8,9,4,2,3,1]
    A_sorted = [1,2,3,4,5,6,7,8,9]
    func(A)
    print("Ok" if A == A_sorted else "Fail")
    
test_sort(sort_insert)