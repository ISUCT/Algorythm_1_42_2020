def shift_up(x, heap):
    while heap[x] > heap[(x-1)//2] and (x-1)//2 >= 0:
        heap[x], heap[(x-1)//2] = heap[(x-1)//2], heap[x]
        x = (x-1)//2
    return x+1

def shift_down(x, heap):
    while 2*x+1 < len(heap):
        left_index = 2*x+1
        right_index = 2*x+2
        index = left_index
        if right_index < len(heap) and heap[left_index] < heap[right_index]:
            index = right_index
        if heap[index] <= heap[x]:
            break
        heap[x], heap[index] = heap[index], heap[x]
        x = index
    return x+1

def add(item, heap):
    heap.append(item)
    return shift_up(len(heap)-1, heap)

def direct_extract(x, heap):
    i = heap[len(heap)-1]
    heap[x-1], heap[len(heap)-1] = heap[len(heap)-1], heap[x-1]
    inda = heap.pop()
    if i < inda: 
        shift_down(x-1, heap)
    elif i > inda:
        shift_up(x-1, heap)
    return inda

def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    inda = heap.pop()
    if heap:
        return shift_down(0, heap), inda
    else:
        return 0, inda

def main():
    heap = []
    res = []
    amount = input().split()
    n, m = int(amount[0]), int(amount[1])
    for amount in range(m):
        data = input().split()
        if int(data[0]) == 1:
            if not heap:
                res.append(-1)
            else:
                res.append(extract(heap))
        elif int(data[0]) == 2:
            if len(heap) == n:
                res.append(-1)
            else:
                res.append(add(int(data[-1]), heap))
        elif int(data[0]) == 3:
            if len(heap) >= int(data[-1]) and int(data[-1]) > 0: 
                res.append(direct_extract(int(data[-1]), heap)) #значение удалённого элемента
            else:
                res.append(-1) 
    for amount in res:
        if type(amount) == tuple:
            print(*amount)
        else:
            print(amount)
    print(*heap)

main() 