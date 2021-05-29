class Node:  
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)

def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right))+1

def building_tree(el):
    root = Node(el[0])
    for i in range(1, len(el)):
        root.add(el[i])
    return root

def blnc(tree):
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) 
    and blnc(tree.right) and blnc(tree.left)):
        return 1
    return 0

def main():
    n = list(map(int,input().split()))
    n.pop()
    tree = building_tree(n)

    if blnc(tree) == 1: 
        print("YES")
    else:
        print("NO")

main()