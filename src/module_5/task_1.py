def task_1():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['7 3 2 1 9 5 4 6 8 0']))  # input
    >>> task_1()
    2
    9 
    """
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

    def build(elm):
        tree = Node(elm[0])
        for i in range(1, len(elm)-1):
            tree.add_branch(elm[i], 1)
        return tree

    list = list(map(int, input().split()))
    tree = build(list)
    tree.find()
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) 