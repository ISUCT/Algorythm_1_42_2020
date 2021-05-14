"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join([\
'7 3 2 1 9 5 4 6 8 0'\
]))
>>> bt = BinaryTree()
>>> bt.insert(5)
>>> print(bt.get_elements())
[5]
>>> bt.insert(1)
>>> print(bt.get_elements())
[1, 5]
>>> bt.insert(3)
>>> print(bt.get_elements())
[1, 3, 5]
>>> bt.insert(7)
>>> print(bt.get_elements())
[1, 3, 5, 7]
>>> bt.find(7)
True
>>> bt.find(2)
False
>>> task_tree()
2
9
"""

class Node():
    def __init__(self, value):
        self.__left = None
        self.right = None
        self.value = value
    
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, left):
        self.__left = left

class BinaryTree():
    def __init__(self):
        self.__size = 0
        self.__root = None
        self.__elements = []
        super().__init__()

    def size(self):
        return self.__size()
    
    def inner_find(self, val, current):
        if not current:
            return False
        elif current.value == val:
            return True
        elif current.value > val:
            return self.inner_find(val, current.left)
        elif current.value < val:
            return self.inner_find(val, current.right)

    def inner_insert(self, val, current):
        if not current:
            self.__size += 1
            return Node(val)
        elif current.value > val:
            current.left = self.inner_insert(val, current.left)
        elif current.value < val:
            current.right = self.inner_insert(val, current.right)
        return current
    
    def inner_traversal(self, current):
        if not current:
            return
        self.inner_traversal(current.left)
        self.__elements.append(current.value)
        self.inner_traversal(current.right)

    def get_elements(self):
        self.__elements = []
        self.inner_traversal(self.__root)
        return self.__elements

    def inner_min(self, current):
        pass

    def find_min(self):
        return self.inner_min(self.__root)

    def insert(self, val):
        self.__root = self.inner_insert(val, self.__root)

    def find(self, val):
        return self.inner_find(val, self.__root)
    pass


def task_tree():
    inp = input()
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)