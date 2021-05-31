from collections import deque
def min_on_section(numbers,properties):
    lenght = properties[0]
    end_index = properties[1]
    minimums = []
    deq = deque()
    for index in range(end_index):
        while (deq) and (numbers[index] < numbers[deq[-1]]):
            deq.pop()
        deq.append(index)
    
    for index in range(end_index, lenght):
        minimums.append(numbers[deq[0]])

        while (deq) and (deq[0] <= index - end_index):
            deq.popleft()
             
        while (deq) and (numbers[index] < numbers[deq[-1]]) :
            deq.pop()
        deq.append(index)

    minimums.append(numbers[deq[0]])

    return minimums

def main():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['7 3','1 3 2 4 5 3 1']))  # input
    >>> main()
    1
    2
    2
    3
    1
    """
    properties = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    minimums = min_on_section(numbers, properties)
    [print(minimum) for minimum in minimums]

if __name__ == "__main__":
   import doctest
   doctest.testmod(verbose=True)