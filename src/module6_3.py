def shift_down(x, heap): 
    while 2*x+1 < len(heap):
        left_index = 2*x+1 
        right_index = 2*x+2
        index = 2*x+1
        if right_index < len(heap) and heap[left_index] < heap[right_index]:
            index = right_index
        if heap[index] <= heap[x]:
            break 
        heap[x], heap[index] = heap[index], heap[x] 
        x = index

def extract(heap): 
    heap[0], heap[-1] = heap[-1], heap[0]
    a = heap.pop()
    shift_down(0, heap)
    return a

def get_max(heap): 
    return heap[0]

def build(arr): #дерево
    heap = arr[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i, heap)
    return heap

def main():
    n = int(input()) 
    res = []
    numbers = list(map(int, input().split()))[:n] #вводим элементы массива
    heap = build(numbers) #куча
    for i in range(n): 
        print(*heap)
        res.append(extract(heap)) 
    res.reverse() 
    print(*res) 

main() 