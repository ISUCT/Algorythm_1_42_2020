class Node:  
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)
        else:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)

def elevation(tree):
    if tree is None:
        return 0
    return max(elevation(tree.right), elevation(tree.left))+1

def binary_tree(el):
    base = Node(el[0])
    for i in range(1, len(el)):
        base.add(el[i])
    return base

def balance(tree):
    if not tree or ((elevation(tree.right) == elevation(tree.left) or elevation(tree.right)+1 == elevation(tree.left) or elevation(tree.right) == elevation(tree.left)+1) 
    and balance(tree.right) and balance(tree.left)):
        return 1
    return 0

def main():
    n = list(map(int,input().split()))
    n.pop()
    tree = binary_tree(n)

    if balance(tree) == 1: 
        print("YES")
    else:
        print("NO")

main()