class treeNode:
    _size = 0 
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
        treeNode._size += 1

    def add(self, amount): 
        if amount == self.data:
            return
        if amount < self.data:
            if self.left:
                self.left.add(amount)
            else:
                self.left = treeNode(amount)
        else:
            if self.right:
                self.right.add(amount)
            else:
                self.right = treeNode(amount)

    def findFork(self): 
        if self.left: 
            self.left.findFork()
        if (self.left and self.right is None) or (self.left is None and self.right): 
            print(self.data) 
        if self.right: 
            self.right.findFork()

def buildTree(elements): 
    result = treeNode(elements[0])
    for i in range(1, len(elements)):
        result.add(elements[i])
    return result

def main():
    numbers = list(map(int, input().split(" "))) 
    numbers.pop() 
    tree = buildTree(numbers) 
    tree.findFork() 

main() 