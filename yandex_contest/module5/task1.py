class Node:
    __size = 0
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        Node.__size += 1
    
    def ff(self):
        if self.left:
            self.left.ff()
        if not self.left and not self.right:
            print(self.data)
        if self.right:
            self.right.ff()
    
    def add(self, value):
        if value == self.data:
            return
        if value < self.data:
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)

    def ff(self):
        if self.left:
            self.left.ff()
        if (self.left and self.right is None) or (self.left is None and self.right):
            print(self.data)
        if self.right:
            self.right.ff()
        
def btree(elements):
    s = Node(elements[0])
    for i in range(1, len(elements)):
        s.add(elements[i])
    return s

numbers = [int(item) for item in input().split()]
numbers.pop()

derevo = btree(numbers)

derevo.ff()