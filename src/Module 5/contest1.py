class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 1
        self.height = 0


    def add_branch(self, value, depth):
        if self.data == value:
            return
        if value < self.data:
            if self.left:
                self.left.add_branch(value, depth+1)
            else:
                if self.height < depth:
                    self.height = depth
                self.left = Node(value)
        else:
            if self.right:
                self.right.add_branch(value, depth+1)
            else:
                if self.height < depth:
                    self.height = depth
                self.right = Node(value)

    def search(self):
        if self.left:
            self.left.find()
        if self.left and not self.right:
            print(self.data)
        if self.right and not self.left:
            print(self.data)
        if self.right:
            self.right.find()

def build_the_tree(numbers):
    tree = Node(numbers[0])
    for i in range(1, len(numbers)-1):
        tree.add_branch(numbers[i], 1)
    return tree

def main():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['7 3 2 1 9 5 4 6 8 0']))  # input
    >>> main()
    2
    9
    """
    numbers = list(map(int, input().split()))
    first_tree = build_the_tree(numbers)
    first_tree.search()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
