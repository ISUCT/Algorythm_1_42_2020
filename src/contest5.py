from typing import Dict
def diffs():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['5','1 0 1 2 0']))  # input
    >>> diffs()
    3
    """
    lenght = int(input())
    numbers = list(map(int,input().split(" ")))
    result: Dict[int, int] = {}
    for item in numbers:
        result[item] = 1
    print(len(result))

#Ниже описан второй способ
def count_diffs():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['5','1 0 1 2 0']))  # input
    >>> count_diffs()
    3
    """
    lenght = int(input())
    numbers = list(map(int,input().split(" ")))
    print(len(set(numbers)))
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
