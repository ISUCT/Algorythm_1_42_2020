# 1 способ   5 тест TL 

#  length, len_wind = (int(i) for i in input().split())
# a = list(map(int,input().split()))
# kek = []
# for i in range(length-len_wind+1):
#     min = 10000
#     if (len_wind <= len(a)):
#         for j in range(len_wind):
#             if a[j] < min:
#                 min = a[j]
#     kek.append(min)
#     a.pop(0)
# for i in range(len(kek)): 
#     print(kek[i])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#2 способ 6 тест TL
# length, len_wind = map(int, input().split())
# kek = list(map(int, input().split()))
# for i in range(length - len_wind + 1):
#     print(min(kek[i:i + len_wind]))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#3 способ 12 тест TL
# def update_min(min_v, new):
#     if new < min_v:
#         min_v = new
#     return min_v

# length, len_wind = (int(i) for i in input().split())
# a = list(map(int,input().split()))
# minimum = min(a[:len_wind])

# print(minimum)

# for i in range(len_wind, len(a)):
#     old,new = a[i - len_wind], a[i]
#     if old == minimum:
#         minimum = min(a[i - len_wind +1:i + 1])
#     minimum = update_min(minimum, new)
#     print(minimum)
#~~~~~~~~~~~~~~~~~~

#4 способ рабочий код
from collections import deque

def scroll_wind(a, length, len_wind):
    deq = deque()

    for i in range(len_wind):
        while (deq) and (a[i] < a[deq[-1]]) :
            deq.pop()
        deq.append(i)

    for i in range(len_wind, length):
        print(a[deq[0]])

        while (deq) and (deq[0] <= i-len_wind):
            deq.popleft()
             
        while (deq) and (a[i] < a[deq[-1]]) :
            deq.pop()
        deq.append(i)

    print(a[deq[0]])

length, len_wind = (int(i) for i in input().split())
a = list(map(int,input().split()))

scroll_wind(a, length, len_wind)                   