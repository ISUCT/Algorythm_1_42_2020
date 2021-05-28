class Node:  
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None

    def add(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.l:
                self.l.add(data)
            else:
                self.l = Node(data)
        else:
            if self.r:
                self.r.add(data)
            else:
                self.r = Node(data)

def height(tree):
    if tree is None:
        return 0
    return max(height(tree.l), height(tree.r))+1

def building_tree(el):
    a = Node(el[0])
    for i in range(1, len(el)):
        a.add(el[i])
    return a

def balance(tree):
    if not tree or ((height(tree.l) == height(tree.r) or height(tree.l)+1 == height(tree.r) or height(tree.l) == height(tree.r)+1) and balance(tree.r) and balance(tree.l)):
        return True
    else:
        return False

def main():
    n = [int(i) for i in input().split()]
    n.pop()
    tree = building_tree(n)

    if balance(tree): 
        print('YES')
    else:
        print('NO')

main()