class Node:
    s = 0
    h = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        Node.s += 1

    @property
    def s_(self):
        return self.s

    @property
    def h_(self):
        return self.h

    def add_branch(self, val, depth):
        if self.data == val:
            return
        if val < self.data:
            if self.left:
                self.left.add_branch(val, depth+1)
            else:
                if Node.h < depth:
                    Node.h = depth
                self.left = Node(val)
        else:
            if self.right:
                self.right.add_branch(val, depth+1)
            else:
                if Node.h < depth:
                    Node.h = depth
                self.right = Node(val)

    def find(self):
        if self.left:
            self.left.find()
        if self.left and not self.right:
            print(self.data)
        if self.right and not self.left:
            print(self.data)
        if self.right:
            self.right.find()

def building_tree(el):
    tree = Node(el[0])
    for i in range(1, len(el)-1):
        tree.add_branch(el[i], 1)
    return tree

list = list(map(int, input().split()))
tree = building_tree(list)
tree.find()