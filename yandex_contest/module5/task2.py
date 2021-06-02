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

def h(tree): 
    if tree is None:
        return 0
    return max(h(tree.left), h(tree.right))+1

def ptree(elements): 
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root

def balans(tree): 
    if not tree or ((h(tree.left) == h(tree.right) or h(tree.left)+1 == h(tree.right) or h(tree.left) == h(tree.right)+1) and balans(tree.right) and balans(tree.left)):
        return True 
    return False 


n = [int(i) for i in input().split()]
n.pop()
tree = ptree(n)

if balans(tree): 
    print("YES") 
else:
    print("NO") 

