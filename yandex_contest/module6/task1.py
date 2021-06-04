def shift_up(idx, heap):
    while heap[idx] > heap[(idx-1) // 2] and (idx-1) // 2 >= 0:
        heap[idx], heap[(idx-1) // 2] = heap[(idx-1) // 2], heap[idx]
        idx = (idx-1) // 2
    return idx + 1

def shift_down(idx, heap):
    while 2 * idx + 1 < len(heap):
        left_index = 2 * idx + 1
        right_index = 2 * idx + 2
        child_index = left_index

        if right_index < len(heap) and heap[left_index] < heap[right_index]:
            child_index = right_index

        if heap[child_index] <= heap[idx]:
            break

        heap[idx], heap[child_index] = heap[child_index], heap[idx]
        idx = child_index
    return idx + 1


def get_max(heap):
    return heap[0]


def add(i, heap):
    heap.append(i)
    return shift_up(len(heap)-1, heap)


def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    idx = heap.pop()
    if heap:
        return shift_down(0, heap), idx
    else:
        return 0, idx


heap = []
result = []
num = input().split()
t1, t2 = int(num[0]), int(num[1])

for _ in range(t2):
    data = input().split()
    if int(data[0]) == 1:
        if heap == []:
            result.append(-1)
        else:
            result.append(extract(heap))

    elif int(data[0]) == 2:
        if len(heap) == t1:
            result.append(-1)
        else:
            result.append(add(int(data[-1]), heap))

for item in result:
    if type(item) == tuple:
        print(*item)
    else:
        print(item)

print(*heap) 