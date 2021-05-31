def shift_up(x, heap): 
    while heap[x] > heap[(x-1)//2] and (x-1)//2 >= 0: 
        heap[x], heap[(x-1)//2] = heap[(x-1)//2], heap[x] 
        x = (x-1)//2  
    return x+1

def shift_down(x, heap): 
    while 2*x+1 < len(heap): 
        left_index = 2*x+1 #идекса левого элемента
        right_index = 2*x+2 #индекса правого элемента
        index = 2*x+1 
        if right_index < len(heap) and heap[left_index] < heap[right_index]: 
            index = right_index 
        if heap[index] <= heap[x]: 
            break 
        heap[x], heap[index] = heap[index], heap[x] 
        x = index 
    return x+1

def add(amount, heap): #добавление вершины
    heap.append(amount) 
    return shift_up(len(heap)-1, heap)

def extract(heap): 
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    x = heap.pop() 
    if heap:
        return shift_down(0, heap), x
    else:
        return 0, x

def main(): 
    heap = [] 
    res = []
    amount = input().split() 
    n, m = int(amount[0]), int(amount[1]) #максимальный размер приоритетной очереди и количество запросов
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
    for i in res: 
        if type(i) == tuple: 
            print(*i) 
        else:  
            print(i) 
    print(*heap) 

main()