from collections import deque
def nearest_min(numbers,length):
    result = [0]*length
    stack = []
    for number in reversed(numbers):
        while (len(stack) > 0) and (stack[-1][0] >= number[0]):
            stack.pop()
        if stack == []:
            result[number[1]] = -1
        else:
            result[number[1]] = stack[-1][1]
        stack.append(number)
    return result

def main():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['10','1 2 3 2 1 4 2 5 3 1']))  # input
    >>> main()
    -1 4 3 4 -1 6 9 8 9 -1
    """
    length = int(input())
    numbers = list(zip(list(map(int, input().split())), range(length)))
    print(' '.join(map(str, nearest_min(numbers,length))))

if __name__ == "__main__":
   import doctest
   doctest.testmod(verbose=True)
