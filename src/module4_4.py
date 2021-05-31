from collections import deque

def scroll_wind(a, lengt, len_wind):
    deq = deque()

    for i in range(len_wind):
        while (deq) and (a[i] < a[deq[-1]]) :
            deq.pop()
        deq.append(i)

    for i in range(len_wind, lengt):
        print(a[deq[0]])

        while (deq) and (deq[0] <= i-len_wind):
            deq.popleft()

        while (deq) and (a[i] < a[deq[-1]]) :
            deq.pop()
        deq.append(i)

    print(a[deq[0]])

lengt, len_wind = (int(i) for i in input().split())
a = list(map(int,input().split()))

scroll_wind(a, lengt, len_wind) 