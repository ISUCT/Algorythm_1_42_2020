from collections import *

class Heap:
    def __init__(self, arr):
        self.arr = arr

    def delete(self):
        self.arr[0], self.arr[self.length-1] = self.arr[self.length-1], self.arr[0]
        max = self.arr.pop()
        self.shift_down(0)
        return max

    def display(self):
        print(*self.arr)

    def shift_down(self, idx):
        while 2 * idx + 1 < self.length:
            left_index = 2 * idx + 1
            right_index = 2 * idx + 2
            child_index = left_index
            if right_index < self.length and self.arr[left_index] < self.arr[right_index]:
                child_index = right_index
            if self.arr[child_index] <= self.arr[idx]:
                break
            self.arr[idx], self.arr[child_index] = self.arr[child_index], self.arr[idx]
            idx = child_index

    @property
    def length(self):
        return len(self.arr)


def bld(arr):
    heap = arr[:]
    first_heap = Heap(heap)
    for item in range(len(heap)-1, -1, -1):
        first_heap.shift_down(item)
    return first_heap


n = int(input())
numbers = list(map(int, input().split()))
heap = bld(numbers)
res = deque()
while heap.length:
    heap.display()
    res.appendleft(heap.delete())
print(*res)