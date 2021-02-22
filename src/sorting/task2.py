"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join(['3',\
'101 80',\
'305 90',\
'200 14'\
]))  # input
>>> task2()
305 90
101 80
200 14

>>> sys.stdin = io.StringIO(chr(10).join([\
'3',\
'20 80',\
'30 90',\
'25 90',\
]))  # input
>>> task2()
25 90
30 90
20 80
"""
def task2():
    n = int(input())
    for i in range(n):
        arr = input()
    print(arr)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)