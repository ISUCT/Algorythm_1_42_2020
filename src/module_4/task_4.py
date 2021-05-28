def task_4():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['7 3', '1 3 2 4 5 3 1']))  # input
    >>> task_4()
    1
    2
    2
    3
    1
    """
    from collections import deque

    def func(n, len, len_w):
        deq = deque()

        for i in range(len_w):
            while deq and (n[i] < n[deq[-1]]) :
                deq.pop()
            deq.append(i)

        for i in range(len_w, len):
            print(n[deq[0]])

            while deq and (deq[0] <= i-len_w):
                deq.popleft()

            while deq and (n[i] < n[deq[-1]]) :
                deq.pop()
            deq.append(i)

        print(n[deq[0]])

    len, len_w = (int(i) for i in input().split())
    n = list(map(int,input().split()))

    func(n, len, len_w)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    
