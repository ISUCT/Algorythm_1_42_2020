class Node:
    size = 0
    height = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        Node.size += 1

    @property
    def size_(self):
        return self.size

    @property
    def height_(self):
        return self.height

    def add_branch(self, val, depth):
        if self.data == val:
            return
        if val < self.data:
            if self.left:
                self.left.add_branch(val, depth+1)
            else:
                if Node.height < depth:
                    Node.height = depth
                self.left = Node(val)
        else:
            if self.right:
                self.right.add_branch(val, depth+1)
            else:
                if Node.height < depth:
                    Node.height = depth
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